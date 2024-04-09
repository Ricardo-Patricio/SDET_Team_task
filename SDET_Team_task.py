import argparse
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

    #call the sync function and sleep with interval
    while True:
        syncFiles(src_path,dst_path,log_path)
        sleep(interval)


if __name__ == "__main__":
    main()  