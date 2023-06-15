# Reddit Comment Bot

This is a simple Python script that logs in to your Reddit account and continuously monitors your most active subreddits for new posts. When a new post is found, the bot will check if the post was made by you and if it has already commented on the post before. If the post meets these criteria, the bot will leave a comment on the post.

## Getting Started

To use this bot, follow these steps:

1. Clone this repository or download the ZIP file.
2. Install the necessary packages by running `pip install -r requirements.txt` in your terminal.
3. Create a new Reddit app at https://www.reddit.com/prefs/apps and note down the client ID and client secret.
4. Create a `config.py` file in the same directory as the `bot.py` file and fill in the following details:
```python
REDDIT_API_APP_ID = 'your_client_id_here'
REDDIT_API_KEY = 'your_client_secret_here'
REDDIT_USERNAME = 'your_username_here'
REDDIT_PASSWORD = 'your_password_here'
COMMENT_TEXT = 'your_comment_text_here'
```
5. Replace the placeholders in the above code with your own Reddit API credentials, username, password, and the text of the comment you want to post.

### Running the Script

There are two methods to run the script: manually or using PM2.

#### Manual Execution

To run the script manually, open a terminal and navigate to the directory where the script files are located. Then, execute the following command:

```bash
python bot.py
```

The bot will start monitoring your most active subreddits for new posts. It will check for new posts every 60 seconds and leave a comment if the post meets the specified criteria.

#### Using PM2 (Ubuntu)

[PM2](https://pm2.keymetrics.io/) is a process manager for Node.js applications. Although the script is written in Python, PM2 can also manage Python scripts. Here's how you can run the script using PM2 on Ubuntu:

1. Install PM2 by following the [official installation guide](https://pm2.keymetrics.io/docs/usage/quick-start/#installation).
2. Create a `deploy.sh` file in the same directory as the script files (`bot.py` and `config.py`). Add the following content to the `deploy.sh` file:

```bash
#!/bin/bash
cd /path/to/script/directory
python bot.py
```

Make sure to replace `/path/to/script/directory` with the actual path to the directory where the script files are located.

3. Make the `deploy.sh` file executable by running the following command:

```bash
chmod +x deploy.sh
```

4. Start the script using PM2 by running the following command:

```bash
sudo pm2 start ./deploy.sh --name reddit-auto-comment-bot
```

The script will now be managed by PM2 and will continue running even after you close the terminal session.

To check the status of the script, you can use the following command:

```bash
pm2 status
```

This will display a list of all processes managed by PM2, including the Reddit Comment Bot.

### Stopping the Script (PM2)

To stop the script managed by PM2, you can use the following command:

```bash
sudo pm2 stop reddit-auto-comment-bot
```

Replace `reddit-auto-comment-bot` with the name you provided when starting the script with PM2.

### Prerequisites

You need to have Python 3.10 installed on your machine to run this script.

You also need to create a Reddit app and obtain your API credentials as described in step 3 above.

### Installing

To install the necessary packages, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Built With

* [PRAW](https://praw.readthedocs.io/en/stable/) - The Python Reddit API Wrapper used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

## Acknowledgments

This script was inspired by the need to automate Reddit commenting for specific use cases. Special thanks to the PRAW developers for providing a reliable and easy-to-use Reddit API wrapper.

If you encounter any issues or have any questions, please open an issue on the GitHub repository.

---

That's it! You now have the updated README with instructions on running the script using PM2 on Ubuntu. If you have any further questions, feel free to ask.