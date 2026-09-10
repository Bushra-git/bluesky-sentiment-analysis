import boto3

BUCKET_NAME = "twitter-sentiment-pipeline-bushra-2026"

s3 = boto3.client("s3")

try:
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        MaxKeys=10
    )

    print("SUCCESS! EC2 can access S3.")

    for obj in response.get("Contents", []):
        print(obj["Key"])

except Exception as e:
    print("S3 CONNECTION FAILED:")
    print(e)
