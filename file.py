import os
import time
import shutil
import subprocess

# Folder paths
source_folder = "C:/Users/user/Downloads/Chief"  # Replace with the folder where the camera saves pictures
uploaded_folder = os.path.join(source_folder, "uploaded")

# Create the uploaded folder if it doesn't exist
os.makedirs(uploaded_folder, exist_ok=True)

# Upload URL
upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

def upload_picture(file_path):
    try:
        # Execute the curl command
        subprocess.run(["curl", "-X", "POST", "-F", f"imageFile=@{file_path}", upload_url], check=True)
        print(f"Uploaded: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upload {file_path}: {e}")

def move_to_uploaded(file_path):
    # Move the file to the uploaded folder
    file_name = os.path.basename(file_path)
    destination = os.path.join(uploaded_folder, file_name)
    shutil.move(file_path, destination)
    print(f"Moved to uploaded: {file_path}")

def monitor_and_upload():
    while True:
        # List all files in the source folder
        files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
        for file in files:
            file_path = os.path.join(source_folder, file)
            # Upload the picture
            upload_picture(file_path)
            # Move the picture to the uploaded folder
            move_to_uploaded(file_path)
            # Wait for 30 seconds before the next upload
            time.sleep(30)

if __name__ == "__main__":
    print("Monitoring folder and uploading pictures...")
    monitor_and_upload()
