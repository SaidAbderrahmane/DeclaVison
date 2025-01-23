import os
import cv2
import shutil
import random


def extract_frames(video_path, output_dir, fps=1):
    """Extract frames from a video at a specified rate."""
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Failed to open video: {video_path}")
        return

    video_name = os.path.basename(video_path).split('.')[0]
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = max(frame_rate // fps, 1)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
            frame_path = os.path.join(output_dir, f"{video_name}_frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    cap.release()
    print(f"Extracted frames from {video_path} to {output_dir}")



# def split_data(input_dir, output_dir, train_ratio=0.7, val_ratio=0.2):
#     """Split the dataset into train, validation, and test sets."""
#     os.makedirs(output_dir, exist_ok=True)
#     categories = os.listdir(input_dir)

#     for category in categories:
#         category_path = os.path.join(input_dir, category)
#         if not os.path.isdir(category_path):
#             continue

#         files = [os.path.join(category_path, f) for f in os.listdir(category_path) if f.endswith(".jpg")]
#         random.shuffle(files)

#         train_split = int(train_ratio * len(files))
#         val_split = int((train_ratio + val_ratio) * len(files))

#         splits = {
#             "train": files[:train_split],
#             "val": files[train_split:val_split],
#             "test": files[val_split:]
#         }

#         for split_name, split_files in splits.items():
#             split_dir = os.path.join(output_dir, split_name, category)
#             os.makedirs(split_dir, exist_ok=True)
#             for file_path in split_files:
#                 shutil.copy(file_path, os.path.join(split_dir, os.path.basename(file_path)))
        
#         # Generate label file for each extracted frame
#         label_dir = os.path.join("Data", "images", "labels")
#         for split_name, split_files in splits.items():
#             split_dir = os.path.join(label_dir, split_name, category)
#             os.makedirs(split_dir, exist_ok=True)
#             for file_path in split_files:
#                 file_name = os.path.basename(file_path)
#                 frame = cv2.imread(file_path)
#                 label_path = os.path.join(label_dir, f"{file_name}.txt")
#                 height, width, _ = frame.shape
#                 center_x = width / 2
#                 center_y = height / 2
#                 class_id = categories[category]
#                 with open(label_path, 'w') as label_file:
#                     label_file.write(f"{class_id} {center_x} {center_y}\n")

#         print(f"Split {category}: Train={len(splits['train'])}, Val={len(splits['val'])}, Test={len(splits['test'])}")


if __name__ == "__main__":
    video_dir = "Data/videos"
    output_dir = "Data/images"
    extracted_frames_dir = "Data/frames"

    # Step 1: Extract frames
    for category in os.listdir(video_dir):
        category_path = os.path.join(video_dir, category)
        if os.path.isdir(category_path):
            output_category_dir = os.path.join(extracted_frames_dir, category)
            os.makedirs(output_category_dir, exist_ok=True)

            for video_file in os.listdir(category_path):
                video_path = os.path.join(category_path, video_file)
                if video_file.endswith((".mp4", ".avi", ".mov", ".MOV")):
                    extract_frames(video_path, output_category_dir,category)

    # Step 2: Organize dataset into train/val/test splits
    split_data(extracted_frames_dir, output_dir, train_ratio=0.7, val_ratio=0.2)
