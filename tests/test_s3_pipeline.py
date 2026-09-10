from src.ingestion.jetstream_client import JetstreamClient
from src.storage.s3_uploader import S3Uploader


client = JetstreamClient()
uploader = S3Uploader()

print("Collecting live Bluesky posts...")

posts = []

for post in client.stream_posts(max_posts=10):
    posts.append(post)
    print(f"Collected: {post['text'][:80]}")

print(f"\nCollected {len(posts)} posts.")

uploader.upload_posts(posts)

print("S3 upload complete!")
