import os
from pathlib import Path
import send2trash
import csv
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class CleanUp():

    def __init__(self, path, file_types):
        self.path = Path(path)
        self.file_types = file_types

    def write_to_csv(self, data, path='deleted_files.csv'):
    # Write to a CSV file the files deleted
        file_exists = os.path.exists(path)
        with open('deleted_files.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, ['File Name', 'File Path', 'Time'])
            if not file_exists:
                writer.writeheader()
            for file in data:
                writer.writerow({'File Name': file.name, 'File Path': file, 'Time': time.ctime()})
    logging.debug("Data written to CSV file")


    def check_all_empty_files(self):
        #check all empty files in the specified path
        empty_files = []
        for file in self.path.rglob('*'):
            if os.path.getsize(file) == 0:
                empty_files.append(file)
        return empty_files
    
    def delete_empty_files(self):
        #delete all empty files in the specified path
        empty_files = self.check_all_empty_files()
        for file in empty_files:
            send2trash.send2trash(file)
        self.write_to_csv(empty_files)
        logging.debug(f"Deleted {len(empty_files)} empty files")
        
    def list_files(self):
        #list files with the specified file types
        files_to_cleanup = []
        for file_type in self.file_types:
            #finds files with the specified file types
            files_to_cleanup.extend(self.path.rglob(f'*{file_type}'))
        return files_to_cleanup

    def delete_files(self):
        #delete files with the specified file types
        files = self.list_files()
        for file in files:
            send2trash.send2trash(file)
            self.write_to_csv(files)
        logging.debug(f"Deleted {len(files)} file(s)")
        

    def check_empty_folders(self):
        #check all empty folders in the specified path
        empty_folders = []
        for folder in self.path.rglob('*'):
            if os.path.getsize(folder) == 0:
                empty_folders.append(folder)
        return empty_folders
    
    def delete_empty_folders(self):
        #delete all empty folders in the specified path
        empty_folders = self.check_empty_folders()
        for folder in empty_folders:
            send2trash.send2trash(folder)
        self.write_to_csv(empty_folders)
        logging.debug(f"Deleted {len(empty_folders)} empty folders")

    def open_csv(self, path='deleted_files.csv'):
        #open the CSV file for deleted files
        del_files = Path(path)
        os.startfile(del_files)


if __name__ == "__main__":
    path = input("Enter the directory path: ").strip()
    file_types = input("Enter file extensions to delete (comma-separated, e.g., .tmp,.log): ").split(',')
    cleanup = CleanUp(path, file_types)
    #cleanup.list_files()
    #cleanup.delete_files()
    cleanup.check_all_empty_files()
    cleanup.delete_empty_files()
    see_deleted_files = input("Do you want to see the deleted files? (y/n): ")
    if see_deleted_files.lower() == "y":
        cleanup.open_csv()
    else:
        print("Thank you for using the program")
