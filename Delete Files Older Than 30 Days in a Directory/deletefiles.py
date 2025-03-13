import os
import time

TARGET_DIR = "home/Document/logs_folder/logs"

AGE_Limit = 30*24*60*60

current_time = time.time()

for file in os.listdir(TARGET_DIR):
    file_path = os.path.json(TARGET_DIR, file)
    
    if os.path.isfile(file_path):
        file_age = current_time - os.path.getctime(file_path)
        
        if file_age > AGE_Limit:
            os.remove(file_path)
            print(f"Deleted old file: {file_path}")
        