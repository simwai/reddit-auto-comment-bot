import calendar
import datetime
import praw
import config
from praw.exceptions import RedditAPIException


class RedditBot(praw.Reddit):
    def __init__(self, client_id, client_secret, username, password):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent="my_bot/0.0.1",
        )
        print("Authenticated as {}".format(self.user.me()))

    def run(self):
        """
        Monitor new posts made by a user and react when a new post is made.
        """
        user = self.redditor(config.REDDIT_USERNAME)

        # Create a stream generator for the user's posts
        post_stream = user.stream.submissions()

        for post in post_stream:
            print("Post found from {}: {}".format(post.author, post.title))

            # Check if the post is within the allowed age limit
            if not self._is_post_recent(post):
                continue

            # Check if I already commented the post with the configured text
            for comment in post.comments:
                if (
                    comment.author == self.user.me()
                    and comment.body == config.COMMENT_TEXT
                ):
                    continue

            try:
                post.reply(config.COMMENT_TEXT)
                print("Created new command for post: {}".format(post))
            except RedditAPIException as e:
                print("Failed to post comment: {}".format(str(e)))

    def _is_post_recent(self, post, max_age=config.MAX_POST_AGE):
        """
        Check if a post is recent based on the provided max_age in months.
        """
        date = datetime.datetime.utcnow()
        current_utc_time = calendar.timegm(date.utctimetuple())
        post_age = (current_utc_time - post.created_utc) / (
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

    if config.DEBUG:
        bot.run()
        exit()

    while True:
        # Schedule bot to run once a day
        if datetime.datetime.now().hour == 0:
            bot.run()
