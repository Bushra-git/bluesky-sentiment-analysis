import json
import boto3
from datetime import datetime, timezone


class S3Uploader:
    BUCKET_NAME = "twitter-sentiment-pipeline-bushra-2026"

    def __init__(self):
        self.s3 = boto3.client("s3")

    def upload_posts(self, posts):
        timestamp = datetime.now(timezone.utc)
        date = timestamp.strftime("%Y-%m-%d")
        filename = timestamp.strftime("bluesky_%Y%m%dT%H%M%SZ.json")

        key = f"raw/date={date}/{filename}"

        data = json.dumps(posts, ensure_ascii=False, indent=2)

        self.s3.put_object(
            Bucket=self.BUCKET_NAME,
            Key=key,
            Body=data.encode("utf-8"),
            ContentType="application/json"
        )

        print(
            f"Uploaded {len(posts)} posts to "
            f"s3://{self.BUCKET_NAME}/{key}"
        )

    def upload_csv(self, filename):
        timestamp = datetime.now(timezone.utc)
        date = timestamp.strftime("%Y-%m-%d")

        key = f"analytics/date={date}/bluesky_sentiment.csv"

        self.s3.upload_file(
            filename,
            self.BUCKET_NAME,
            key,
            ExtraArgs={
                "ContentType": "text/csv"
            }
        )

        print(
            f"Uploaded analytics CSV to "
            f"s3://{self.BUCKET_NAME}/{key}"
        )
