import time
import datetime
import os
import sys
import logging
import pyinputplus as pyip
import random
from pathlib import Path
import subprocess
import csv
import psutil
from file_types import file_types

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create class for time
class Pomodoro():
    def __init__(self):
        self.target_time = pyip.inputInt("How many minutes would you like to set the timer for? ")
        self.break_min = pyip.inputInt("How many minutes would you like to set the break timer for? ")
        self.path = Path(__file__) #Path to the containing rewards
        self.sessions = 0

    def start_or_not(self):
        choice = pyip.inputYesNo("Would you like to start the Pomodoro timer? ")
        if choice == "yes":
            return True
        else:
            return False

    def minutes_to_seconds(self, minutes):
        """Convert minutes to seconds."""
        return minutes * 60

    def break_time(self):
        """Determines if it's time for a short or long break and runs the countdown."""
        now = datetime.datetime.now()

        if self.sessions % 4 == 0:  # Long break after 4 sessions
            logging.debug("Time for a long break!")
            long_break = now + datetime.timedelta(minutes=self.break_min * 3)  # Long break is 3x normal
        else:
            logging.debug("Time for a short break!")
            long_break = now + datetime.timedelta(minutes=self.break_min)

        while datetime.datetime.now() < long_break:
            remaining_time = (long_break - datetime.datetime.now()).seconds
            sys.stdout.write(f"\rTime Left: {remaining_time // 60}:{remaining_time % 60:02d}   ")  # Extra spaces to clear old text
            sys.stdout.flush()
            time.sleep(1)

        logging.debug("Break time is over! Time to get back to work!")

    def play_reward_and_close_app(self, file_types):
        arr = []

        for dirpath, _, filenames in os.walk(self.path):
            arr.extend(os.path.join(dirpath, file) for file in filenames if any(file.endswith(ext) for ext in file_types))

        if arr:
            logging.debug("Starting to display image...")
            arr_path = random.choice(arr)
            proc = subprocess.Popen(["start", arr_path], shell=True)

            # Wait til break time is over
            self.break_time()

            # Get the name of the default app
            viewer_name = None
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['pid'] == proc.pid:  # Try to match the process ID
                    viewer_name = process.info['name']
                    break

            # If we couldn't find the process by PID, check common file viewers
            if not viewer_name:
                common_media_apps = {
                    "Photos", "mspaint", "IrfanView", "Photoshop", "VLC", "MediaMonkey",
                    "MusicBee", "Media Player", "5KPlayer", "GOM Player", "PotPlayer",
                    "MPV", "KMPlayer", "Quicklook", "Preview", "IINA", "Kodi", "DivX"
                        }

                # Check for the process
                viewer_name = None
                for process in psutil.process_iter(['pid', 'name']):
                    if any(viewer in process.info['name'] for viewer in common_media_apps):
                        viewer_name = process.info['name']
                        proc_id = process.info['pid']
                        break

                # Kill the process if found
                if viewer_name:
                    try:
                        os.system(f"taskkill /IM {viewer_name} /F")
                        logging.debug(f"Closed: {viewer_name}")
                    except Exception as e:
                        logging.error(f"Error closing {viewer_name}: {e}")
        else:
            logging.debug("No media app process found.")

    def play_reward(self):
        reward_choices = {
            "1": "Video",
            "2": "Music",
            "3": "Image",
        }

        print("\nReward Options:")
        for key, value in reward_choices.items():
            print(f"{key}. {value}")
        choice = pyip.inputInt(prompt="Choose your reward type: ")

        if choice == 1:
            self.play_reward_and_close_app(file_types[ "Videos"])
            
        elif choice == 2:
            self.play_reward_and_close_app(file_types["Music"])
           
        elif choice == 3:
            self.play_reward_and_close_app(file_types["Images"])

                
    def start(self):
        if self.start_or_not():
            logging.debug(f"Session {self.sessions + 1} is starting!")
            self.sessions += 1
            now = datetime.datetime.now()
            one_minute = now + datetime.timedelta(minutes=self.target_time)

            while datetime.datetime.now() < one_minute:
                remaining_time = (one_minute - datetime.datetime.now()).seconds
                sys.stdout.write(f"\rTime Left: {remaining_time // 60}:{remaining_time % 60:02d}")
                sys.stdout.flush()
                time.sleep(1)

            logging.debug("Time to take a break!")
            watch_video = pyip.inputYesNo("Would you like to have a reward? (yes/no): ")
            if watch_video == "yes":
                self.play_reward()
                # self.break_time()
            choice_2 = pyip.inputYesNo("Would you like to terminate pomodoro? (yes/no): ")
            if choice_2 == "yes":
                self.quit()
            else:
                self.start()
        else:
            self.quit()

    def log_number_of_sessions(self, sessions):
        file = Path(__file__).parent / "sessions.csv"

        with open(file, "a", newline="") as f:
            filewriter = csv.DictWriter(f, fieldnames=["sessions", "time"])

            if not file.exists() or file.stat().st_size == 0:
                filewriter.writeheader()

            filewriter.writerow({"sessions": str(self.sessions), "time": str(datetime.datetime.now())})

    def quit(self):
        logging.debug(f"You completed {self.sessions} session(s)!")

        save_progress = pyip.inputYesNo("Would you like to save your progress? (yes/no): ")
        if save_progress == "yes":
            self.log_number_of_sessions(self.sessions)

        logging.debug("Goodbye! 😊")
        sys.exit()

if __name__ == "__main__":
    pomodoro = Pomodoro()
    logging.debug(pomodoro.path)
    # pomodoro.play_reward()
    pomodoro.start()