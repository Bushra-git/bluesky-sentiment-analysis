import json
import websocket


class JetstreamClient:
    BASE_URL = (
        "wss://jetstream2.us-east.bsky.network/subscribe"
        "?wantedCollections=app.bsky.feed.post"
    )

    def stream_posts(self, max_posts=10):
        ws = websocket.create_connection(self.BASE_URL, timeout=30)

        count = 0

        try:
            while count < max_posts:
                message = ws.recv()

                if not message:
                    continue

                event = json.loads(message)

                if event.get("kind") != "commit":
                    continue

                commit = event.get("commit", {})

                if commit.get("operation") != "create":
                    continue

                if commit.get("collection") != "app.bsky.feed.post":
                    continue

                record = commit.get("record", {})

                post = {
                    "did": event.get("did"),
                    "rkey": commit.get("rkey"),
                    "text": record.get("text", ""),
                    "created_at": record.get("createdAt"),
                }

                yield post
                count += 1

        finally:
            ws.close()
