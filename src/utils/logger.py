import logging
from src.config.config import Config

def setup_logger(name):
    """Set up and return a logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(Config.LOG_LEVEL)
    
    # Create console handler
    handler = logging.StreamHandler()
    handler.setLevel(Config.LOG_LEVEL)
    
    # Create formatter
    formatter = logging.Formatter(Config.LOG_FORMAT)
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger 