import os

# Specify the path to the folder containing your images
folder_path = './'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter out only image files (you can customize this based on your file types)
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Sort the image files to ensure they are renamed in order
image_files.sort()

# Rename each image file in the desired format
for i, image_file in enumerate(image_files, start=1):
    new_name = f'bg_{i}{os.path.splitext(image_file)[1]}'  # Construct the new name
    old_path = os.path.join(folder_path, image_file)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Images renamed successfully.")
