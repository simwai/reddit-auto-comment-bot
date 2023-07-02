## Reddit Auto Comment Bot
[![VS Code](https://img.shields.io/badge/IDE-VS_Code-blue?logo=visual-studio-code)](https://code.visualstudio.com/)
[![Code style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg)](https://github.com/psf/black)
[![Qodana](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/qodana.yml/badge.svg)](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/qodana.yml)
[![CodeQL](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/codeql.yml/badge.svg?branch=main&event=push)](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/codeql.yml) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The code you see here represents a Python script that automates commenting on new posts made by a specific Reddit user. It utilizes the PRAW library, which provides a convenient wrapper for the Reddit API.

### Prerequisites

Before you can execute and deploy this script, make sure you have the following prerequisites installed:

For execution:
- Python 3.6 (https://www.python.org/downloads/)
(Worked also with 3.11 on Windows)
- PRAW library (install using `pip install praw`)

For deployment on a Linux VPS:
- pm2 (Process Manager for Node.js, can be installed via `npm install pm2 -g`)

### Configuration

To configure the script, you need to provide the necessary credentials in a separate configuration file named `config.py`. Ensure you have the following information available:

- `REDDIT_API_APP_ID`: The client ID of your Reddit API application.
- `REDDIT_API_KEY`: The client secret key of your Reddit API application.
- `REDDIT_USERNAME`: Your Reddit username.
- `REDDIT_PASSWORD`: Your Reddit password.
- `COMMENT_TEXT`: The text you want the bot to comment on new posts.

Copy the config.py.example file and enter your configuration parameters between the string characters ("").

### Running the Script

To execute the script and deploy it with pm2, follow these steps:

1. Clone the repository using the following command:
   ```
   git clone https://github.com/simwai/reddit-auto-comment-bot
   ```
   This will download the code, including the `deploy.sh` script.

2. Navigate to the project directory:
   ```
   cd reddit-auto-comment-bot
   ```
3. Install the required dependencies:
   ```
   python3.6 -m pip install praw
   ```
4. Configure the `config.py` file as mentioned in the previous section.

5. Make sure the `deploy.sh` script is executable:
   ```
   chmod +x deploy.sh
   ```
6. Deploy the script using pm2:
   ```
   sudo ./deploy.sh
   ```
7. Start the script as a pm2 process with a specified name:
   ```
   pm2 start ./deploy.sh --name reddit-auto-comment-bot --interpreter python3.6
   ```

Now, the Reddit auto comment bot is up and running, ready to monitor new posts and comment on them based on your configured comment text.

## License

This project is licensed under the [MIT License](LICENSE).
