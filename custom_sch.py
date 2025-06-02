import subprocess
import os
import time
import json
from datetime import datetime, timedelta

def load_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading config file: {e}")
        return None

def execute_batch_file(batch_file_path):
    # Check if the batch file exists
    if not os.path.exists(batch_file_path):
        print(f"Batch file {batch_file_path} does not exist.")
    else:    
        # Execute the batch file
        try:
            subprocess.run(batch_file_path, shell=True, check=True)
            print(f"Executed batch file: {batch_file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing batch file: {e}")




def schedule_batch_file(single_task, delimiter):
    # Parse the program info to get batch file path and execution time
    try:
        batch_file_path, scheduled_time_str = single_task.split(delimiter) ### DELIMITER IS A HERE ###
        scheduled_time = datetime.strptime(scheduled_time_str.strip(), "%Y%b%d %H:%M")
    except Exception as e:
       print(f"Error occurred while scheduling the task: {e}")
    except ValueError:
        print("Invalid input format. Expected 'batch_file_path;YYYYMONDD HH:MM'.")
        return
    
    # Loop to check the current time and compare with scheduled time
    print(f"Scheduled task for {batch_file_path} at {scheduled_time}")
    
    while True:
        current_time = datetime.now()
        
        # Check if current time matches the scheduled time
        if current_time >= scheduled_time:
            execute_batch_file(batch_file_path)
            break
        
        print(f"Current time: {current_time}")
        print(f"Scheduled time: {scheduled_time}")
        # Sleep for 1 second before checking again
        time.sleep(1)



# Function to read tasks from a file
def read_input_from_file(tasks_file):
    try:
        # Open the file and read the first line (input string)
        # CHANGE PATH HERE WHEN USING ON A DIFFERENT DEVICE/FOLDER
        with open(tasks_file, 'r') as file:
            
            lines = file.readlines()       

        return [line.strip() for line in lines if line.strip()]
        
    except Exception as e:
        print(f"Error reading file: {e}")
        return None




# Function to read tasks from a file and schedule them
def process_tasks_from_file(tasks_file, delimiter):
    tasks = read_input_from_file(tasks_file)

    if tasks:
        for task in tasks:
            schedule_batch_file(task, delimiter)
    else:
        print("No tasks to process.")




# Function to reset scheduled tasks for the next day
def reset_scheduled_tasks(tasks):
    new_tasks = []
    for task in tasks:
        batch_file_path, scheduled_time_str = task.split(',')
        scheduled_time = datetime.strptime(scheduled_time_str.strip(), "%Y%b%d %H:%M")
        
        # Move the scheduled time to the next day
        new_time = scheduled_time + timedelta(days=1)
        formatted_new_time = new_time.strftime("%Y%b%d %H:%M")

        # Add the new task with the updated time
        new_tasks.append(f"{batch_file_path}, {formatted_new_time}")

    return new_tasks




def constantly_check_tasks():
     # Load the configuration file
    config = load_config()
    
    if not config:
        print("Error: Configuration file not found or invalid.")
        return
    
    tasks_file = config.get("tasks_file", "tasks.txt")
    delimiter = config.get("delimiter", ",") 

    tasks = read_input_from_file(tasks_file)

    #infinite loop to check for tasks every day at midnight
    while True:
        if tasks:
            print("Checking for scheduled tasks...")
            process_tasks_from_file(tasks_file, delimiter)

            tasks = reset_scheduled_tasks(tasks)
            print("Tasks have been reset for the next day.")

        current_time = datetime.now()
        midnight = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        sleep_time = (midnight - current_time).total_seconds()
        print(f"Sleeping until midnight: {midnight}")
        time.sleep(sleep_time)

constantly_check_tasks()