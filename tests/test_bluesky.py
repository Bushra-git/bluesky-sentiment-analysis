from src.ingestion.bluesky_client import BlueskyClient


client = BlueskyClient()

result = client.search_posts(
    query="AI",
    limit=10
)

posts = result.get("posts", [])

print(f"Retrieved {len(posts)} posts")

for post in posts:
    author = post.get("author", {}).get("handle", "unknown")
    text = post.get("record", {}).get("text", "")

    print("-" * 60)
    print(f"Author: {author}")
    print(f"Text: {text}")
