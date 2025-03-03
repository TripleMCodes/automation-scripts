import os
import shutil
from pathlib import Path
import send2trash
import time
from file_types import file_types

class Sort_file():
    """Sort files in a given directory"""

    def __init__(self, file_types, p):
        """file types and file path"""
        self.file_types = file_types
        self.p = Path(p)

    def get_unique_filename(self, destination, filename):
            """Generates a unique filename by appending a number if the file already exists."""
            base, ext = os.path.splitext(filename)
            counter = 1
            new_filename = filename

            while os.path.exists(os.path.join(destination, new_filename)):
                new_filename = f"{base}_{counter}{ext}"
                counter += 1
            return new_filename  
    
    def log_session_start(self):
            filename = "files_moved.txt"
            with open(filename, "a") as f:
                f.write("\n")
                f.write("****Files moved at " + str(time.ctime()) + "****")  
        

    def files_moved(self, f_name, src, dst):
            filename = "files_moved.txt"
            with open(filename, "a") as f:
                f.write("\n")
                f.write(str(f_name) + " moved from " + str(src) +  " to " + str(dst) + " at " + str(time.time()))
                f.write("\n")    

    def vid_move(self):
            """Moves vidoes to vidoes folder and creates one if it doesn't already exist"""
            self.log_session_start()
            for dirnames, subdirs, files in os.walk(self.p):
                for f in files:
                    for ext in self.file_types["Videos"]:
                        if f.endswith(ext):
                            try:
                                p_check = self.p.joinpath("Videos")
                                if not p_check.exists():
                                    os.makedirs(p_check)
                                
                                if os.path.exists(os.path.join(p_check, f)) and os.path.exists(os.path.join(self.p, f)):
                                    f_copy = self.get_unique_filename(p_check, f)
                                    shutil.copy(Path(self.p / f), Path(self.p / "Videos" / f_copy))  # Copy the original file
                                    send2trash.send2trash(Path(self.p / f))
                                    self.files_moved(f, self.p, p_check)
                                    print("Done")
                                else:
                                    shutil.move(Path(self.p / f), p_check)  # Move it if it doesn’t exist
                                    self.files_moved(f, self.p, p_check)
                                    print("done")
                            except (PermissionError, shutil.SameFileError, FileNotFoundError) as e:
                                print(e)
                            except OSError as e:
                                pass
    
    def document_move(self):
            """Moves document to Document folder and creates one if it doesn't already exist"""
            self.log_session_start()
            for dirnames, subdirs, files in os.walk(self.p):
                for f in files:
                    for ext in self.file_types["Documents"]:
                        if f.endswith(ext):
                            try:
                                p_check = self.p.joinpath("Documents")
                                if not p_check.exists():
                                    os.makedirs(p_check)
                                
                                if os.path.exists(os.path.join(p_check, f)) and os.path.exists(os.path.join(self.p, f)):
                                    f_copy = self.get_unique_filename(p_check, f)
                                    shutil.copy(Path(self.p / f), Path(self.p / "Documents" / f_copy))  # Copy the original file
                                    send2trash.send2trash(Path(self.p / f))
                                    self.files_moved(f, self.p, p_check)
                                    print("Done")
                                else:
                                    shutil.move(Path(self.p / f), p_check)  # Move it if it doesn’t exist
                                    self.files_moved(f, self.p, p_check)
                                    print("done")
                            except (PermissionError, shutil.SameFileError, FileNotFoundError) as e:
                                print(e)
                            except OSError as e:
                                pass    

    def music_move(self):
            """Moves audio to Music folder and creates one if it doesn't already exist"""
            self.log_session_start()
            for dirnames, subdirs, files in os.walk(self.p):
                for f in files:
                    for ext in self.file_types["Music"]:
                        if f.endswith(ext):
                            try:
                                p_check = self.p.joinpath("Music")
                                if not p_check.exists():
                                    os.makedirs(p_check)
                                
                                if os.path.exists(os.path.join(p_check, f)) and os.path.exists(os.path.join(self.p, f)):
                                    f_copy = self.get_unique_filename(p_check, f)
                                    shutil.copy(Path(self.p / f), Path(self.p / "Music" / f_copy))  # Copy the original file
                                    send2trash.send2trash(Path(self.p / f))
                                    self.files_moved(f, self.p, p_check)
                                    print("Done")
                                else:
                                    shutil.move(Path(self.p / f), p_check)  # Move it if it doesn’t exist
                                    self.files_moved(f,self.p, p_check)
                                    print("done")
                            except (PermissionError, shutil.SameFileError, FileNotFoundError) as e:
                                print(e)
                            except OSError as e:
                                pass
    
    def img_move(self):
            """Moves images to image folder and creates one if it doesn't already exist"""
            self.log_session_start()
            for dirnames, subdirs, files in os.walk(self.p):
                for f in files:
                    for ext in self.file_types["Images"]:
                        if f.endswith(ext):
                            try:
                                p_check = self.p.joinpath("Images")
                                if not p_check.exists():
                                    os.makedirs(p_check)
                                
                                if os.path.exists(os.path.join(p_check, f)) and os.path.exists(os.path.join(self.p, f)):
                                    f_copy = self.get_unique_filename(p_check, f)
                                    shutil.copy(Path(self.p / f), Path(self.p / "Images" / f_copy))  # Copy the original file
                                    send2trash.send2trash(Path(self.p / f))
                                    self.files_moved(f, self.p, p_check)
                                    print("Done")
                                else:
                                    shutil.move(Path(self.p / f), p_check)  # Move it if it doesn’t exist
                                    self.files_moved(f, self.p, p_check)
                                    print("done")
                            except (PermissionError, shutil.SameFileError, FileNotFoundError) as e:
                                print(e)
                            except OSError as e:
                                pass    
    def others_move(self):
            """Moves others to others' folder and creates one if it doesn't already exist"""
            self.log_session_start()
            for dirnames, subdirs, files in os.walk(self.p):
                #all file extentions
                all_ext = (self.file_types["Images"] + self.file_types["Documents"] + self.file_types["Videos"] + self.file_types["Music"])
                for f in files:
                    if not any(f.endswith(ext) for ext in all_ext):
                            try:
                                p_check = Path(self.p / "Others")
                                if not p_check.exists():
                                    os.makedirs(p_check)
                                
                                if os.path.exists(os.path.join(p_check, f)) and os.path.exists(os.path.join(self.p, f)):
                                    f_copy = self.get_unique_filename(p_check, f)
                                    shutil.copy(Path(self.p / f), Path(self.p / "Others" / f_copy))  # Copy the original file
                                    send2trash.send2trash(Path(self.p / f))
                                    self.files_moved(f, self.p, p_check)
                                    print("Done")
                                else:
                                    shutil.move(Path(self.p / f), p_check)  # Move it if it doesn’t exist
                                    self.files_moved(f, self.p, p_check)
                                    print("done")
                            except (PermissionError, shutil.SameFileError) as e:
                                print(e)
                            except OSError as e:
                                pass
                            except FileNotFoundError as e:
                                print(e)
                                break
    def main():
        p = "" #directory path
        sorter = Sort_file(file_types, p)
        sorter.vid_move()
        sorter.document_move()
        sorter.img_move()
        sorter.music_move()
        sorter.others_move()

if __name__ == "__main__":
    Sort_file.main()
