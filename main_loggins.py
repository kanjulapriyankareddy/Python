import logging
import os

LOG_DIR = "loggings"
LOG_FILE_NAME = "app.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    force=True
)

from math_utiloggings import *

#logging.info(add(6,9))

#logging.info(sub(6,3))

logging.info(multiply(2,2))


logging.info(divide(2,4))


