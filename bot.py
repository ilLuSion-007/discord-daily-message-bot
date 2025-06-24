import os
import discord
from discord.ext import tasks
import datetime
import pytz
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # The ID of your general channel

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    send_daily_message.start()

@tasks.loop(hours=24)
async def send_daily_message():
    # Get IST timezone
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist)
    
    # Check if it's 10:00 PM IST
    if current_time.hour == 22 and current_time.minute == 0:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("Sat Shri Akal Nu Sab Nu!")
            print(f"Message sent at {current_time}")

# Start the bot
if __name__ == "__main__":
    bot.run(TOKEN) 