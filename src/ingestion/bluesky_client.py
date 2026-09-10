import requests


class BlueskyClient:
    BASE_URL = "https://api.bsky.app/xrpc/app.bsky.feed.searchPosts"

    def search_posts(self, query="AI", limit=10):
        params = {
            "q": query,
            "sort": "latest",
            "limit": limit,
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=30
        )

        response.raise_for_status()
        return response.json()
