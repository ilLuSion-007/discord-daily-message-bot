# Discord Daily Message Bot

A Discord bot that posts "Sat Shri Akal Nu Sab Nu!" message daily at 10:00 PM IST in your specified channel.

## Project Structure

```
discord-daily-message-bot/
├── src/
│   ├── bot/
│   │   └── bot.py           # Main bot implementation
│   ├── config/
│   │   └── config.py        # Configuration settings
│   ├── utils/
│   │   └── logger.py        # Logging utility
│   └── main.py              # Application entry point
├── .env.example             # Example environment variables
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Features

- Sends daily message at 10:00 PM IST
- Proper error handling and logging
- Configurable message and timing
- Clean project structure
- Easy to maintain and extend

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd discord-daily-message-bot
   ```

2. **Create a Discord Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name
   - Go to the "Bot" section and click "Add Bot"
   - Under the "Privileged Gateway Intents" section, enable "Message Content Intent"
   - Copy the bot token

3. **Invite the Bot to Your Server**
   - Go to OAuth2 > URL Generator
   - Select "bot" under scopes
   - Select "Send Messages" under bot permissions
   - Use the generated URL to invite the bot to your server

4. **Get Channel ID**
   - Enable Developer Mode in Discord (Settings > Advanced > Developer Mode)
   - Right-click on your general channel and select "Copy ID"

5. **Setup Environment**
   - Copy `.env.example` to `.env`
   - Fill in your bot token and channel ID in the `.env` file

6. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Run the Bot**
   ```bash
   python src/main.py
   ```

## Hosting Options

1. **Railway.app** (Recommended for beginners)
   - Free tier available
   - Easy deployment
   - Automatic restarts
   - Visit [Railway.app](https://railway.app/) to get started

2. **Heroku**
   - Reliable hosting
   - Easy deployment
   - Visit [Heroku](https://www.heroku.com/) to get started

3. **DigitalOcean**
   - More advanced option
   - Full control over the server
   - Visit [DigitalOcean](https://www.digitalocean.com/) to get started

4. **Oracle Cloud Free Tier**
   - Always free tier available
   - Good for long-term hosting
   - Visit [Oracle Cloud](https://www.oracle.com/cloud/free/) to get started

## Customization

You can customize the bot's behavior by modifying the following:

1. **Message Content**: Edit `DAILY_MESSAGE` in `src/config/config.py`
2. **Timing**: Modify `TARGET_HOUR` and `TARGET_MINUTE` in `src/config/config.py`
3. **Timezone**: Change `TIMEZONE` in `src/config/config.py`

## Important Notes

- Make sure to keep your bot token secure and never share it
- The bot needs to be running 24/7 to send messages at the specified time
- Consider using a process manager like PM2 if hosting on a VPS
- The bot uses IST (Indian Standard Time) for scheduling messages
- All errors are logged for easy debugging

## Contributing

Feel free to submit issues and enhancement requests! 