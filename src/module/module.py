# TODO add doc string for module
from logger import logger

log = logger.get_logger(__name__)
# TODO What does this do exactly with the dunder method


# TODO DocString for this func
def multiply(num1: int, num2: int) -> int:
    log.debug("Executing multiply function.")
    return num1 * num2
