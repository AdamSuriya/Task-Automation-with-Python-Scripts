import os
import shutil
from datetime import datetime

# Define the source directory
source_directory = "/path/to/your/source_directory"

# Define destination directories
text_files_directory = "/path/to/your/text_files_directory"
image_files_directory = "/path/to/your/image_files_directory"

# Define the log file path
log_file_path = "/path/to/your/log_file.log"

# Function to log actions
def log_action(action):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{current_time} - {action}\n")
    print(action)

# Function to rename files by appending the current date
def rename_files():
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Loop through all files in the source directory
    for filename in os.listdir(source_directory):
        old_file_path = os.path.join(source_directory, filename)
        
        # Only process files (skip directories)
        if os.path.isfile(old_file_path):
            new_filename = f"{current_date}_{filename}"
            new_file_path = os.path.join(source_directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            log_action(f"Renamed file: {filename} -> {new_filename}")

# Function to move files to their respective directories based on extension
def move_files():
    for filename in os.listdir(source_directory):
        old_file_path = os.path.join(source_directory, filename)
        
        # Only process files (skip directories)
        if os.path.isfile(old_file_path):
            # Determine the file extension
            file_extension = filename.split('.')[-1].lower()
            
            # Move text files to the text_files directory
            if file_extension == 'txt':
                new_file_path = os.path.join(text_files_directory, filename)
                shutil.move(old_file_path, new_file_path)
                log_action(f"Moved file: {filename} to {text_files_directory}")
            
            # Move image files (like jpg, png) to the image_files directory
            elif file_extension in ['jpg', 'jpeg', 'png']:
                new_file_path = os.path.join(image_files_directory, filename)
                shutil.move(old_file_path, new_file_path)
                log_action(f"Moved file: {filename} to {image_files_directory}")
            else:
                log_action(f"File {filename} has an unsupported extension, not moved.")

# Function to list all files in the source directory
def list_files():
    files = os.listdir(source_directory)
    print("\nFiles in the source directory:")
    for filename in files:
        print(filename)

# Function to execute the automation
def execute_automation():
    print("Starting the task automation...\n")
    
    # Step 1: List all files in the source directory
    list_files()

    # Step 2: Rename files by appending current date
    rename_files()
    
    # Step 3: Move files based on their extension
    move_files()

    print("\nTask automation completed!")

if __name__ == "__main__":
    execute_automation()
