import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def split_video_into_parts(video_path, start_time_str, part_duration_min=4):
    # 1. Convert the start time to seconds
    try:
        parts = list(map(int, start_time_str.split(':')))
        if len(parts) == 3:  # HH:MM:SS
            start_time = parts[0] * 3600 + parts[1] * 60 + parts[2]
        elif len(parts) == 2:  # MM:SS
            start_time = parts[0] * 60 + parts[1]
        else:
            start_time = int(start_time_str)
    except ValueError:
        print("❌ Invalid time format. Please provide MM:SS or HH:MM:SS.")
        return

    # 2. Load the video
    video_path = video_path.strip('"').strip("'")
    if not os.path.exists(video_path):
        print("❌ Could not find the video file! Check the path.")
        return
        
    clip = VideoFileClip(video_path)
    video_duration = clip.duration
    part_duration_sec = part_duration_min * 60

    # 3. Create the output folder
    output_folder = "Output_Parts"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("--- Video splitting started ---")
    
    current_start = start_time
    part_number = 1

    # 4. Split the video into parts
    while current_start < video_duration:
        current_end = current_start + part_duration_sec
        
        if current_end > video_duration:
            current_end = video_duration

        output_filename = os.path.join(output_folder, f"Part_{part_number}.mp4")
        
        print(f"🎬 Cutting Part {part_number} ({current_start}s to {current_end}s)...")
        
        # Here we use .subclipped to match the newer MoviePy version instead of .subclip
        sub_clip = clip.subclipped(current_start, current_end)
        sub_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")
        
        current_start = current_end
        part_number += 1

    clip.close()
    print("====================================================")
    print(f"✅ All done! Saved in the '{output_folder}' folder.")
    print("====================================================")

# --- Program Run ---
if __name__ == "__main__":
    print("===================================")
    print("Video Splitter by Lakshitha Madumal")
    print("===================================")
    video_location = input("Enter the video file path: ")
    start_at = input("Enter the start time to split from (HH:MM:SS): ")
    duration_min = input("Enter the split duration in minutes (whole number): ")
    try:
        duration_min = int(duration_min)
        if duration_min <= 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid duration. Please enter a positive whole number of minutes.")
    else:
        split_video_into_parts(video_location, start_at, part_duration_min=duration_min)
