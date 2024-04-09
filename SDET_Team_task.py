import argparse
import os
from pathlib import Path
from time import sleep

def syncFiles(src_path, dst_path, log_path):
    return 0
    

def main():
    parser = argparse.ArgumentParser(description="Folder sync")

    #Source folder path argument (String)
    parser.add_argument("src", type=str, help="Source path")
    #Replica folder path argument (String)
    parser.add_argument("dst", type=str, help="Replica path")
    #Synchorization interval argument (int)
    parser.add_argument("interval", type=int, help="Sync time interval")
    #Log path argument (String)
    parser.add_argument("log", type=str, help="Log path")
    args = parser.parse_args()
    
    #Command arguments into variables
    src_path = Path(args.src)
    dst_path = Path(args.dst)
    interval = args.interval
    log_path = args.log

    #check if source folders exists
    if not os.path.exists(src_path):
        raise FileNotFoundError("The source directory does not exist.") 
    
    #check if replica folders exists
    if not os.path.exists(dst_path):
        raise FileNotFoundError("The replica directory does not exist.")
    
    #check if log file exists
    if not os.path.exists(log_path):
        #create the file if it does not exist
        print("Log file has been created")
        open(log_path, "a+")
    
    #call the sync function and with given interval
    while True:
        syncFiles(src_path,dst_path,log_path)
        sleep(interval)


if __name__ == "__main__":
    main()  