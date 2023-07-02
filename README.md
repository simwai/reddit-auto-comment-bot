## Reddit Auto Comment Bot
[![IDE: VS Code](https://img.shields.io/badge/IDE-VS_Code-blue?logo=visual-studio-code)](https://code.visualstudio.com/)
[![Style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg)](https://github.com/psf/black)
[![Quality: Qodana](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/qodana.yml/badge.svg)](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/qodana.yml)
[![Security: CodeQL](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/codeql.yml/badge.svg?branch=main&event=push)](https://github.com/simwai/reddit-auto-comment-bot/actions/workflows/codeql.yml) 
[![License: MIT](https://img.shields.io/badge/License-MIT-mediumpurple.svg)](https://opensource.org/licenses/MIT)

The code you see here represents a Python script that automates commenting on new posts made by a specific Reddit user. It utilizes the PRAW library, which provides a convenient wrapper for the Reddit API.

### Prerequisites

Before you can execute and deploy this script, make sure you have the following prerequisites installed:

For execution:
- Python (https://www.python.org/downloads/) </br>
(Somehow 3.10.x makes problems, so don't use this Python version, I recommend 3.9.x or 3.11.x LTS)
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
   python -m pip install praw
   ```
4. Configure the `config.py` file as mentioned in the previous section.

5. Make sure the `deploy.sh` script is executable:
   ```
   sudo chmod +x deploy.sh
   ```
6. Deploy the script using pm2:
   ```
   sudo ./deploy.sh
   ```
7. Start the script as a pm2 process with a specified name:
   ```
   pm2 start ./index.py --name reddit-auto-comment-bot --interpreter python --log-date-format="HH:mm DD-MM-YYYY" --restart-delay=0
   ```
Now, the Reddit auto comment bot is up and running, ready to monitor new posts and comment on them based on your configured comment text.

## License

This project is licensed under the [MIT License](LICENSE).
