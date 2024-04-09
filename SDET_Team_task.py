import argparse
import os
import datetime
import shutil
from pathlib import Path
from time import sleep


def syncFiles(src_path, dst_path, log_path):

    #get the file list from source and replica folders
    src_dir = os.listdir(src_path)
    dst_dir = os.listdir(dst_path)

    with open(log_path, 'a+') as log_file_handle:
        
        #remove the obsolete files from replica that dont exist in source folder
        for file in dst_dir:
            path_file_dst = os.path.join(dst_path,file)
            #check if file is not in source folder
            if file not in src_dir:
                #check if its a file
                if os.path.isfile(path_file_dst):
                    os.remove(path_file_dst)
                    print(f"File: {file} has been removed from replica folder\n")
                    # Write the removal message to the log file          
                    log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ": File " + file + " has been removed from replica folder\n")
                
                #check if its a folder and its not in source folder
                if os.path.isdir(path_file_dst):
                    shutil.rmtree(path_file_dst)
                    print(f"Folder {file} has been removed from replica folder\n")
                    # Write the removal message to the log file          
                    log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ": Folder " + file + " has been removed from replica folder\n")

        #sync the folders
        for file in src_dir:
            path_file_src = os.path.join(src_path,file)
            path_file_dst = os.path.join(dst_path,file)
            
            #check if its a file and if it exists in replica folder
            if os.path.isfile(path_file_src):
                if os.path.exists(path_file_dst):
                    shutil.copy(path_file_src,path_file_dst)
                    print(f"File: {file} has been overwriten\n")
                    # Write the overwritten message to the log file          
                    log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + f" {file} has been overwriten\n")
                else:
                    shutil.copy(path_file_src,path_file_dst)
                    print(f"File: {file} has been created\n")
                    # Write the creation message to the log file          
                    log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + f" {file} has been created\n")
            
            #check if its a folder
            if os.path.isdir(path_file_src):
                if os.path.exists(path_file_dst):
                    #if it exists remove the contents of the folder
                    shutil.rmtree(path_file_dst)
                    shutil.copytree(path_file_src,path_file_dst)
                    print(f"Folder: {file} has been overwriten\n")
                    # Write the overwritten message to the log file          
                    log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + f" {file} folder has been overwriten\n")
                else:
                    shutil.copytree(path_file_src,path_file_dst)
                    print(f"Folder: {file} has been created\n")
                    # Write the overwritten message to the log file          
                    log_file_handle.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + f" {file} folder has been overwriten\n")
    

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


    #check if log file exists
    if not os.path.exists(log_path):
        #create the file if it does not exist
        print("Log file has been created\n")
        open(log_path, "a+").close()

    #call the sync function and with given interval
    while True:

        #check if source folders exists
        if not os.path.exists(src_path):
            raise FileNotFoundError("The source directory does not exist.") 
    
        #check if replica folders exists
        if not os.path.exists(dst_path):
            raise FileNotFoundError("The replica directory does not exist.")
        
        syncFiles(src_path,dst_path,log_path)
        sleep(interval)


if __name__ == "__main__":
    main()  