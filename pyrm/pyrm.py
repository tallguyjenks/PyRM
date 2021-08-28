"""This is the main function entry point of the application
TODO this section needs to be more copiously documented
"""

from loguru import logger

logger.add("logs/app.log", backtrace=True, diagnose=True)

logger.debug("Starting")
logger.debug("Finishing.")
