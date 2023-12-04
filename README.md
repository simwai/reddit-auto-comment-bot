## Reddit Auto Comment Bot
[![IDE: VS Code](https://img.shields.io/badge/IDE-VS_Code-blue?logo=visual-studio-code)](https://code.visualstudio.com/)
[![Style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-mediumpurple.svg)](https://opensource.org/licenses/MIT)

The code you see here represents a Python script that automates commenting on new posts made by a specific Reddit user. It utilizes the PRAW library, which provides a convenient wrapper for the Reddit API.

### Prerequisites

Before you can execute or deploy this script, make sure you have the following prerequisites installed:

For execution:
- Python (https://www.python.org/downloads/)

For deployment on a Linux VPS:
- pm2 (Process Manager for Node.js, can be installed via `npm install pm2 -g`)

### Configuration

To configure the script, you need to provide the necessary credentials in a separate configuration file named `config.py`. Ensure you have the following information available:

### Required Configuration Parameters

#### Reddit API Credentials

`REDDIT_API_APP_ID` - The client ID for your Reddit API application. This uniquely identifies your app to Reddit's API. 

`REDDIT_API_KEY` - The client secret key for your Reddit API application. Used to authenticate your app.

`REDDIT_USERNAME` - The username of the Reddit account the bot will use to perform actions. 

`REDDIT_PASSWORD` - The password for the Reddit account specified in `REDDIT_USERNAME`.

#### Bot Behavior 

`COMMENT_TEXT` - The text the bot will post as a comment on new posts it finds.

`MAX_POST_AGE` - The maximum age (in months) of posts the bot will search and comment on. Posts older than this will be ignored.

`DEBUG` - When true, runs the bot immediately instead of scheduling it and exits. For development/testing.


Copy the config.py.example file and enter your configuration parameters.

### Running the Script

To execute the script or deploy it on a Linux VPS:

1. Clone the repository using the following command:
   ```
   git clone https://github.com/simwai/reddit-auto-comment-bot
   ```

2. Navigate to the project directory:
   ```
   cd reddit-auto-comment-bot
   ```

3. Configure the `config.py` file as mentioned in the previous section.

4. (Windows) Run the script with
   ```
   deploy.bat
   ```

5. (Linux VPS) Make sure the `deploy.sh` script is executable:
   ```
   sudo chmod +x deploy.sh
   ```

6. (Linux VPS) Run the script manually
   ```
   sudo ./deploy.sh
   ```
   or start the script as a pm2 process with a specified name:
   ```
   pm2 start ./index.py --name reddit-auto-comment-bot --interpreter python --log-date-format="HH:mm DD-MM-YYYY"
   ```

Now, the Reddit auto comment bot is up and running, ready to monitor new posts and comment on them based on your configuration.

## License

This project is licensed under the [MIT License](LICENSE).
