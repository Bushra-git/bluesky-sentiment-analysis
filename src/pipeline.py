import pandas as pd

from src.ingestion.jetstream_client import JetstreamClient
from src.processing.sentiment_processor import SentimentProcessor
from src.storage.s3_uploader import S3Uploader


def main():
    client = JetstreamClient()
    processor = SentimentProcessor()
    uploader = S3Uploader()

    posts = []

    print("Listening for live Bluesky posts...")

    for post in client.stream_posts(max_posts=50):
        text = post.get("text", "")

        if not text.strip():
            continue

        sentiment = processor.analyze(text)

        processed_post = {
            "post_id": f"{post['did']}/{post['rkey']}",
            "author_did": post["did"],
            "created_at": post["created_at"],
            "text": text,
            "sentiment_label": sentiment["sentiment_label"],
            "sentiment_score": sentiment["sentiment_score"],
            "positive_score": sentiment["positive_score"],
            "neutral_score": sentiment["neutral_score"],
            "negative_score": sentiment["negative_score"],
        }

        posts.append(processed_post)

        print("-" * 60)
        print(f"Text: {text[:100]}")
        print(f"Sentiment: {sentiment['sentiment_label']}")
        print(f"Score: {sentiment['sentiment_score']}")

    if not posts:
        print("No posts collected.")
        return

    df = pd.DataFrame(posts)

    df["created_at"] = pd.to_datetime(
        df["created_at"],
        format="mixed",
        utc=True
    )

    df["date"] = df["created_at"].dt.date.astype(str)
    df["hour"] = df["created_at"].dt.hour

    output_file = "data/bluesky_sentiment.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved analytics dataset to {output_file}")

    uploader.upload_posts(posts)
    uploader.upload_csv(output_file)
    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()
