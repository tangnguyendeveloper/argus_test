from argus_tool import argus, argus_client
import time
import logging

APP_NAME = "ArgusTest"
INTERFACE = "eth0"
DURATION = 60

if __name__ == "__main__":
    
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s', "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    started, process = argus.start_argus(
        path_to_argus = '/usr/local/sbin/argus',
        interface = INTERFACE,
        server_port = 561
    )
    
    if not started:
        logger.warning(f"The argus server is running PID = {process}.")
    else:
        while True:
            logger.info("Waiting for the argus server ...")    
            time.sleep(3)
            
            is_running, pid = argus.is_argus_server_running()
            if is_running:
                logger.info(f"The argus server is running PID = {pid}.")
                break
    
    
    logger.info(f"Geting network flow of {INTERFACE} in {DURATION} seconds.")    
    error, df_metric = argus_client.get_metric(
        path_to_ra = "/usr/local/bin/ra",
        server = "localhost",
        port = 561,
        duration_in_secands = DURATION,
    )
    
    if error:
        logger.error(error)
    else:
        print(df_metric)
        # df_metric is Pandas DataFrame, can convert to tensor for ML/DL

    if started:
        argus.kill_argus(process)
    else:
        argus.kill_argus()
        
    while True:
        logger.info("Stopping for the argus server ...")    
        time.sleep(3)
        is_running, pid = argus.is_argus_server_running()
        if not is_running:
            logger.info("The argus server is stoped.")
            break
