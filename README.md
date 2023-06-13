# Reddit Comment Bot

This is a simple Python script that logs in to your Reddit account and continuously monitors your most active subreddits for new posts. When a new post is found, the bot will check if the post was made by you and if it has already commented on the post before. If the post meets these criteria, the bot will leave a comment on the post.

## Getting Started

To use this bot, follow these steps:

1. Clone this repository or download the ZIP file.
2. Install the necessary packages by running `pip install -r requirements.txt` in your terminal.
3. Create a new Reddit app at https://www.reddit.com/prefs/apps and note down the client ID and client secret.
4. Create a `config.py` file in the same directory as the `bot.py` file and fill in the following details:
```
REDDIT_API_APP_ID = 'your_client_id_here'
REDDIT_API_KEY = 'your_client_secret_here'
REDDIT_USERNAME = 'your_username_here'
REDDIT_PASSWORD = 'your_password_here'
COMMENT_TEXT = 'your_comment_text_here'
```
5. Replace the placeholders in the above code with your own Reddit API credentials, username, password, and the text of the comment you want to post.
6. Run the bot by running `python bot.py` in your terminal.

The bot will continue checking for new posts every 60 seconds until you stop the program manually.

### Prerequisites

You need to have Python 3.x installed on your machine to run this script. You also need to create a Reddit app and obtain your API credentials as described in step 3 above.

### Installing

To install the necessary packages, run the following command in your terminal:
```
pip install -r requirements.txt
```

## Built With

* [PRAW](https://praw.readthedocs.io/en/stable/) - The Python Reddit API Wrapper used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.