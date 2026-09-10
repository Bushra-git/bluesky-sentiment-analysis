from src.processing.sentiment_processor import SentimentProcessor


processor = SentimentProcessor()

test_posts = [
    "I absolutely love this new technology!",
    "This is terrible and completely disappointing.",
    "Today is a normal day."
]

for text in test_posts:
    result = processor.analyze(text)

    print("-" * 60)
    print(f"Text: {text}")
    print(f"Sentiment: {result['sentiment_label']}")
    print(f"Score: {result['sentiment_score']}")
