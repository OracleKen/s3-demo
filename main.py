import boto3

client = boto3.client('s3')

print('starting file read and upload')

with open('hello.txt', "rb") as data:
    client.upload_fileobj(data, "oracleken-s3-demo", "hello.txt")

files = client.list_objects(Bucket="oracleken-s3-demo")

for files in files["Contents"]:
    print(files["Key"])

print('done')

print('starting file downlad')

with open("helloworld2.txt", "wb") as file:
    client.download_fileobj("oracleken-s3-demo", "hello.txt", file)

print("file created and downloaded")


print('delete hello.txt')

client.delete_object(Bucket="oracleken-s3-demo", Key="hello.txt")


print('File deleted')

files = client.list_objects(Bucket="oracleken-s3-demo")

for files in files["Contents"]:
    print(files["Key"])
