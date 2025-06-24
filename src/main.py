from src.bot.bot import run_bot
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

if __name__ == "__main__":
    logger.info("Starting Discord Daily Message Bot...")
    run_bot() 