import argparse
import os
import datetime
from pathlib import Path
from time import sleep

def syncFiles(src_path, dst_path, log_path):

    #get the file list from source and replica folders
    src_dir = os.listdir(src_path)
    dst_dir = os.listdir(dst_path)
    
    #open the log file
    with open(log_path, 'a+') as log_file_handle:
    #remove the obsolete files from replica that dont exist in source folder
        for file in dst_dir:
            path_file_dst = os.path.join(dst_path,file)
            #check if file is not in source folder
            if file not in src_dir:
                #if its not remove it
                os.remove(path_file_dst)
                print("File " + file + " has been removed from replica folder\n")
                # Write the removal message to the log file
                log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ": File " + file + " has been removed from replica folder\n")

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
        print("Log file has been created\n")
        open(log_path, "a+").close()
    
    #call the sync function and with given interval
    while True:
        syncFiles(src_path,dst_path,log_path)
        sleep(interval)


if __name__ == "__main__":
    main()  