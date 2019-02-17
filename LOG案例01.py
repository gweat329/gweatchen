import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %P"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.basicConfig(level=logging.DEBUG)
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error")
logging.critical("this is critical")