# TODO add doc string for module
import logging

from rich.logging import RichHandler

APP_LOGGER_NAME = "pyrm"


# TODO DocString for this func
def setup_applevel_logger(logger_name=APP_LOGGER_NAME, file_name=None):  # noqa: E302
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    shell_formatter = logging.Formatter("%(message)s")
    shell_handler = RichHandler()
    shell_handler.setFormatter(shell_formatter)

    logger.handlers.clear()
    logger.addHandler(shell_handler)

    if file_name:
        file_formatter = logging.Formatter(
            "%(levelname)s - %(asctime)s - %(name)s - [%(filename)s:%(funcName)s:%(lineno)d] - %(message)s"
        )
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    return logger


# TODO DocString for this func
def get_logger(module_name):
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)


try:
    with open("logs/app.log") as file:
        _log = logging.getLogger(APP_LOGGER_NAME)
        _log.setLevel(logging.DEBUG)
        _shell_formatter = logging.Formatter("%(message)s")
        _shell_handler = RichHandler()
        _shell_handler.setFormatter(_shell_formatter)
        _log.handlers.clear()
        _log.addHandler(_shell_handler)
        _log.debug("Log File Found at /logs/app.log")
        _log.debug(f"{file}")
except FileNotFoundError:
    with open("logs/app.log", "w+"):
        # TODO LEV G
        pass
    exit()
