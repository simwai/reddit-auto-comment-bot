import praw
import time
import config

# Configure the Reddit API credentials
reddit = praw.Reddit(
    client_id=config.REDDIT_API_APP_ID,
    client_secret=config.REDDIT_API_KEY,
    user_agent="CommentBot",
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD,
)

# Get a list of the 5 subreddits where you are most active
target_subreddits = [
    submission.subreddit.display_name
    for submission in reddit.redditor(name=config.REDDIT_USERNAME).submissions.new(
        limit=5
    )
]


# Define the comment you want the bot to post
my_url = "https://simwai.taplink.ws"
comment_text = f"Hey there!\n\nI'd like to share a link with you: [My Taplink]({my_url}). There you'll find more of my projects and ways to donate me. \n\nIf you appreciate what I do and would like to show your support, a small donation would mean a lot! Every contribution helps me continue my efforts. Thank you in advance!"


# Create a function to monitor new posts and post comments
def monitor_and_comment():
    while True:
        print("Checking for new posts...")

        for subreddit_name in target_subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.new(limit=10):
                # Check if the submission is made by you
                if submission.author == reddit.user.me():
                    # Check if the submission is already commented by the bot
                    if not any(
                        comment.author == reddit.user.me()
                        for comment in submission.comments
                    ):
                        # Post a comment on your own submission
                        submission.reply(comment_text)

        # Wait for 60 seconds before checking for new posts again
        time.sleep(60)


# Start monitoring and commenting
monitor_and_comment()
