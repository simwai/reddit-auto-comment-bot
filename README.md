## Reddit Auto Comment Bot

The code you see here represents a Python script that automates commenting on new posts made by a specific Reddit user. It utilizes the PRAW library, which provides a convenient wrapper for the Reddit API.

### Prerequisites

Before you can execute and deploy this script, make sure you have the following prerequisites installed:

- Python 3.10 (https://www.python.org/downloads/) 
  (You can use another Python 3.x too. For that, use your local configured Python commands in the deploy script and during the installation process.
- PRAW library (install using `pip install praw`)
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
   git clone <repository_url>
   ```
   This will download the code, including the `deploy.sh` script.

2. Navigate to the project directory:
   ```
   cd <project_directory>
   ```

3. Install the required dependencies:
   ```
   python3.10 -m pip install praw
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
   pm2 start ./deploy.sh --name reddit-auto-comment-bot
   ```

Now, the Reddit auto comment bot is up and running, ready to monitor new posts and comment on them based on your configured comment text.
