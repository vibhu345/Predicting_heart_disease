import logging
from datetime import datetime
import os
# creating a Log file
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#LOG_FILE= f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
# defining the directry (folder path) which points to "LOGSSSSSS" folder only
log_dir=os.path.join(os.getcwd(),"LOGSSSSSS")
# ceating the directry safely
os.makedirs(log_dir,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_dir,LOG_FILE)

logging.basicConfig(
            level=logging.INFO,
             format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
             filename=LOG_FILE_PATH
             )
if __name__=="__main__":
    logging.info("logging ho rhi hai")
