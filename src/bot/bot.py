import discord
from discord.ext import tasks
import datetime
import pytz
from src.config.config import Config
from src.utils.logger import setup_logger

# Initialize logger
logger = setup_logger(__name__)

class DailyMessageBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.daily_message.start()

    async def on_ready(self):
        """Called when the bot is ready and connected to Discord."""
        logger.info(f'{self.user} has connected to Discord!')
        logger.info(f'Bot is in {len(self.guilds)} guilds')

    @tasks.loop(hours=24)
    async def daily_message(self):
        """Send daily message at the specified time."""
        try:
            # Get IST timezone
            ist = pytz.timezone(Config.TIMEZONE)
            current_time = datetime.datetime.now(ist)
            
            # Check if it's the target time
            if (current_time.hour == Config.TARGET_HOUR and 
                current_time.minute == Config.TARGET_MINUTE):
                
                channel = self.get_channel(Config.CHANNEL_ID)
                if channel:
                    await channel.send(Config.DAILY_MESSAGE)
                    logger.info(f"Message sent at {current_time}")
                else:
                    logger.error(f"Could not find channel with ID {Config.CHANNEL_ID}")
        except Exception as e:
            logger.error(f"Error in daily_message task: {str(e)}")

    async def on_error(self, event_method, *args, **kwargs):
        """Handle any errors that occur during bot operation."""
        logger.error(f"Error in {event_method}: {str(args[0])}")

def run_bot():
    """Run the bot with error handling."""
    try:
        client = DailyMessageBot()
        client.run(Config.TOKEN)
    except Exception as e:
        logger.error(f"Failed to start bot: {str(e)}")
        raise 