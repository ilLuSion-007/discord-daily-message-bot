import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Bot Configuration
    TOKEN = os.getenv('DISCORD_TOKEN')
    CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
    
    # Message Configuration
    DAILY_MESSAGE = "Sat Shri Akal Nu Sab Nu!"
    TIMEZONE = 'Asia/Kolkata'
    TARGET_HOUR = 22  # 10 PM
    TARGET_MINUTE = 0
    
    # Logging Configuration
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_LEVEL = 'INFO' 