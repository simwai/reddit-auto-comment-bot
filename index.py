import praw
import config
from praw.exceptions import RedditAPIException


class RedditBot:
    def __init__(self, client_id, client_secret, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.reddit = None

    def authenticate(self):
        """
        Authenticate to Reddit API using the provided credentials.
        """
        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=self.username,
            password=self.password,
            user_agent="my_bot/0.0.1",
        )
        print("Authenticated as {}".format(self.reddit.user.me()))

    def run(self):
        """
        Monitor new posts made by a user and react when a new post is made.
        """
        user = self.reddit.redditor("simwai")

        # Create a stream generator for the user's posts
        post_stream = user.stream.submissions()

        for post in post_stream:
            print("New post by {}: {}".format(post.author, post.title))
            # Check if already commented on the post
            if post.author == self.reddit.user.me():
                continue

            # Check if the post is within the allowed age limit
            if not self.is_post_recent(post):
                continue

            try:
                post.reply(config.COMMENT_TEXT)
            except RedditAPIException as e:
                print("Failed to post comment: {}".format(str(e)))

    def is_post_recent(self, post, max_age=6):
        """
        Check if a post is recent based on the provided max_age in months.
        """
        current_time = self.reddit.user.me().created_utc
        post_age = (current_time - post.created_utc) / (
            60 * 60 * 24 * 30
        )  # Convert to months
        return post_age <= max_age


if __name__ == "__main__":
    bot = RedditBot(
        client_id=config.REDDIT_API_APP_ID,
        client_secret=config.REDDIT_API_KEY,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
    )

    bot.authenticate()
    bot.run()
