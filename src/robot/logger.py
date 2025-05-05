"""
Logging module for the autonomous robot.
"""

import logging
import sys
from datetime import datetime

def setup_logger(name='robot', level=logging.INFO):
    """
    Set up a logger for the robot.
    
    Args:
        name (str): Name of the logger
        level (int): Logging level
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(f'robot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Create default logger instance
logger = setup_logger() 