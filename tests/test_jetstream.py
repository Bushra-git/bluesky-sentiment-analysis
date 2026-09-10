from src.ingestion.jetstream_client import JetstreamClient


client = JetstreamClient()

print("Listening for Bluesky posts...")

for post in client.stream_posts(max_posts=10):
    print("-" * 60)
    print(f"DID: {post['did']}")
    print(f"Created: {post['created_at']}")
    print(f"Text: {post['text']}")
