import cv2
import os

def extract_keyframes(video_path, threshold=5000):
    base_dir = "data"
    output_dir = os.path.join(base_dir, "keyframes")
    os.makedirs(output_dir, exist_ok=True)
    video = cv2.VideoCapture(video_path)
    success, prev_frame = video.read()
    frame_count = 0

    while success:
        success, current_frame = video.read()
        if not success:
            break
        diff = cv2.absdiff(prev_frame, current_frame)
        non_zero_count = cv2.countNonZero(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY))
        if non_zero_count > threshold:
            keyframe_path = os.path.join(output_dir, f"keyframe_{frame_count}.jpg")
            cv2.imwrite(keyframe_path, current_frame)
        prev_frame = current_frame
        frame_count += 1

    video.release()


# Example usage

for filename in os.listdir("Data/videos"):
    if filename.endswith(".mp4"):
        extract_keyframes(os.path.join("Data/videos", filename))

