import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
#

log_path=os.path.join(os.getcwd(),"logs")
# Create a custom logger, which will write to a file
# logs folder will be created in the root directory

os.makedirs(log_path,exist_ok=True)
# Create a custom logger, which will write to a file

LOG_FILEPATH=os.path.join(log_path,LOG_FILE)
#

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)