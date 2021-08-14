from File import s3

if __name__ == '__main__':
    client = s3(profile_name="boaz")
    # 버킷 생성
    # client.create_bucket("boaz-taebin")

    # 버킷 업로드
    # client.upload_bucket_data(
    #     bucketname="boaz-taebin", filename="network1.pdf", fileurl="file")

    # 버킷 다운로드
    # client.download_bucket_file(
    #     bucketname="boaz-taebin", key="network1.pdf", fileurl="image")

    # 버킷 데이터 확인
    # client.get_buket_files_name(bucketname="boaz-taebin")

    # 버킷 데이터 여러개 다운로드
    client.download_buket_files(
        bucketname="boaz-taebin", prefix="", dir="test2", allfiles=True)

    # 버킷 데이터 삭제
    # client.delete_file(bucket_name="boaz-taebin",
    #                    filename="network1.pdf")
