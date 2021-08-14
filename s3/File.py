import boto3
import os
import re


class s3:
    def __init__(self, profile_name):
        # S3 Client 생성
        self.session = boto3.Session(profile_name=profile_name)
        self.s3 = self.session.client('s3')

    def get_bucket_list(self, toReturn=False):
        # S3에있는 현재 버킷리스트의 정보를 가져온다.
        response = self.s3.list_buckets()
        print(response)
        # # response에 담겨있는 Buckets의 이름만 가져와 buckets 변수에 배열로 저장.
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        # # S3 버킷 리스트를 출력.
        print("Bucket List: %s" % buckets)
        if toReturn:
            return buckets

    # 주의할점! 이름 중복에 주의해야한다. 관련 오류는 밑에 있음
    # when calling the CreateBucket operation: The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.
    def create_bucket(self, name, locaction=None):
        if locaction is None:
            location = 'ap-northeast-2'
        try:
            self.s3.create_bucket(Bucket=name,
                                  CreateBucketConfiguration={'LocationConstraint': location})
            print("create bucket successful")
        except Exception as e:
            print("failed create bucket")
            print(e)

    def upload_bucket_data(self, bucketname, filename, fileurl=None):
        # 첫본째 매개변수 : 로컬에서 올릴 파일이름
        # 두번째 매개변수 : S3 버킷 이름
        # 세번째 매개변수 : 버킷에 저장될 파일 이름.
        server_file_name = filename
        if fileurl is not None:
            server_file_name = fileurl+"/"+filename
        try:
            self.s3.upload_file(filename, bucketname, server_file_name)
            print("successful upload file")
        except Exception as e:
            print("failed upload file")
            print(e)

    # prefix ex) image/test
    def get_buket_files_name(self, bucketname, prefix=None, toReturn=False):
        if prefix is None:
            prefix = ""
        paginator = self.s3.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=bucketname,
            Prefix=prefix
        )
        Key = []
        for page in response_iterator:
            for content in page['Contents']:
                if not toReturn:
                    print(content["Key"])
                else:
                    Key.append(content["Key"])
        if toReturn:
            return Key

    def download_bucket_file(self, bucketname, key, fileurl=None):
        download_loc = key
        if fileurl is not None:
            self.__create_folder(fileurl)
            download_loc = fileurl+"/"+key.split("/")[-1]
        self.s3.download_file(bucketname, key, download_loc)

    # prefix ex) image/test
    def download_buket_files(self, bucketname, prefix=None, dir=None, allfiles=True):
        if prefix is None:
            prefix = ""
        else:
            prefix += "/"

        if dir is None:
            dir = ""
        else:
            dir = dir+"/"
            self.__create_folder(dir)

        if allfiles:
            prefix_cnt = -1
        else:
            prefix_cnt = len(prefix.split("/"))

        paginator = self.s3.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=bucketname,
            Prefix=prefix
        )
        self.__download_data(response_iterator, bucketname, dir, prefix_cnt)

    def delete_file(self, bucket_name, filename, fileurl=None):
        server_file_name = filename
        if fileurl is not None:
            server_file_name = fileurl+"/"+filename
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=server_file_name)
            print("successful delete file")
        except Exception as e:
            print("failed delete file")
            print(e)

    def __download_data(self, response_iterator, bucketname, dir, prefix_cnt):
        try:
            for page in response_iterator:
                for content in page['Contents']:
                    if (len(content["Key"].split("/")) == prefix_cnt) | (prefix_cnt == -1):
                        if prefix_cnt != -1:
                            prefix_cnt = prefix_cnt - 1
                        if self.__check_file(content['Key']):
                            self.session.resource('s3')\
                                .Bucket(bucketname)\
                                .download_file(content['Key'], dir+content['Key'].split("/")[prefix_cnt])
            print("success download file")
        except Exception as e:
            print("failed download file")
            print(e)

    def __check_file(self, data):
        pattern = re.compile("\w*.*[a-z]")
        result = pattern.match(data)
        return bool(result)

    def __create_folder(self, dir):
        # os를 활용해서 폴더 만들기
        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print("not create folder")
