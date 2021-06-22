# TODO add doc string for module
import logger

# This will create the log file if it doesn't yet exist
# !The logger needs to be initialized before the other module imports
log = logger.setup_applevel_logger(file_name="src/logs/app.log")
import module  # noqa: E402

log.debug("Calling module function.")
module.multiply(5, 2)
log.debug("Finished.")
