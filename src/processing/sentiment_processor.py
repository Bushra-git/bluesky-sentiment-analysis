from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentProcessor:

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        scores = self.analyzer.polarity_scores(text)

        compound = scores["compound"]

        if compound >= 0.05:
            label = "positive"
        elif compound <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        return {
            "sentiment_label": label,
            "sentiment_score": compound,
            "positive_score": scores["pos"],
            "neutral_score": scores["neu"],
            "negative_score": scores["neg"],
        }
