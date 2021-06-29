"""This is the main function entry point of the application
TODO this section needs to be more copiously documented
"""

from loguru import logger

logger.add("logs/app.log", backtrace=True, diagnose=True)


def sum(num1: int, num2: int) -> int:
    """
    Sum of 2 numbers

    Args:
        num1 (int): First number to add
        num2 (int): Second number to add

    Returns:
        int: Result aggregate sum
    """
    return num1 + num2


logger.debug("Starting")
logger.debug("Finishing.")
