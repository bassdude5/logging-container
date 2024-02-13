import time
import logging
import configparser

# Logging encoding
ENCODING = "utf-8"

# Config file name
CFG_FILENAME = "config.ini"

# Config section name
SECT_NAME = "SECTION_NAME"

# Log default filename (if not set in the cfg file)
log_filename = "test.log"

def isNotBlank(s):
    return bool(s and not s.isspace())

def initializeLogger(cfg_log_filename):
    if isNotBlank(cfg_log_filename):
        log_filename = cfg_log_filename

    logging.basicConfig(filename=log_filename, encoding=ENCODING, level=logging.INFO, format='%(asctime)s - %(message)s')

def readCfgFile():
    # Read config.ini file
    config_object = configparser.RawConfigParser()
    config_object.read(CFG_FILENAME)
    return config_object[SECT_NAME]

def loop(log_interval):

    i = 0
    while(i < 5):
        # print(log_interval)
        logging.info("Time Interval: %i", i)
        i = i + 1
        time.sleep(int(log_interval))

# Main
def main():

    # Read the config file
    cfgInfo = readCfgFile()
    # print(cfgInfo["log_filename"])
    
    # Setup the logger
    initializeLogger(cfgInfo["log_filename"])

    # Start looping and logging
    loop(cfgInfo["log_interval"])
    # print("Password is {}".format(userinfo["log_interval"]))


if __name__ == '__main__':
    main()
