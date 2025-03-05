'''pre processing the dataset and converting the dataset into yolo format.'''


import os
import shutil

def create_yolo_folders(base_path):
    folders = ['train/images', 'train/labels', 'val/images', 'val/labels']
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Folder Created: {path}")

def move_files(src_folder, dest_folder, file_ext):
    files = [f for f in os.listdir(src_folder) if f.endswith(file_ext)]
    for file in files:
        shutil.copy(os.path.join(src_folder, file), os.path.join(dest_folder, file))
    print(f"Moved {len(files)} {file_ext} files to {dest_folder}")

if __name__ == "__main__":
    BASE_PATH = "dataset"

    create_yolo_folders(BASE_PATH)

    # Move Image Files
    move_files("dataset/images/train", "dataset/train/images", ".jpg")
    move_files("dataset/images/val", "dataset/val/images", ".jpg")

    # Move Label Files
    move_files("dataset/labels/train", "dataset/train/labels", ".txt")
    move_files("dataset/labels/val", "dataset/val/labels", ".txt")

    print("Dataset Preprocessing Completed!")
