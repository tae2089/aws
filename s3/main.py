from File import s3

if __name__ == '__main__':
    client = s3(profile_name="default")
    # 버킷 생성
    # client.create_bucket("test-taebin")
    buckname = ""
    filename = ""
    # 버킷 업로드
    # url = client.upload_bucket_data(
    #     bucketname=buckname, filename=filename)
    # print(url)
    client.get_version_file(bucket_name=buckname,filename=filename)
    # 버킷 다운로드
    # client.download_bucket_file(
    #     bucketname=buckname, key="network1.pdf", fileurl="image")

    # 버킷 데이터 확인
    # client.get_buket_files_name(bucketname=buckname)

    # 버킷 데이터 여러개 다운로드
    # client.download_buket_files(
    #     bucketname=buckname, prefix="", dir="test2", allfiles=True)

    # 버킷 데이터 삭제
    # client.delete_file(bucket_name=buckname,
    #                    filename="network1.pdf")
