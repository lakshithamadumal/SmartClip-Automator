import os
import random
from moviepy.video.io.VideoFileClip import VideoFileClip

def split_video_into_parts(video_path, start_time_str, min_duration_min=3, max_duration_min=5):
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

    # 3. Create the output folder
    output_folder = "Output_Parts"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("--- Video splitting started ---")
    print(f"💡 Each part will have a random duration between {min_duration_min}-{max_duration_min} minutes")
    
    current_start = start_time
    part_number = 1

    # 4. Split the video into parts with random durations
    while current_start < video_duration:
        # Generate random duration between min and max (in seconds)
        random_duration_min = random.randint(min_duration_min, max_duration_min)
        part_duration_sec = random_duration_min * 60
        current_end = current_start + part_duration_sec
        
        if current_end > video_duration:
            current_end = video_duration

        output_filename = os.path.join(output_folder, f"Part_{part_number}.mp4")
        
        # Convert seconds to MM:SS format for display
        start_min, start_sec = divmod(int(current_start), 60)
        end_min, end_sec = divmod(int(current_end), 60)
        duration_min_display, duration_sec_display = divmod(int(current_end - current_start), 60)
        
        print(f"🎬 Cutting Part {part_number} ({start_min}:{start_sec:02d} to {end_min}:{end_sec:02d}) - Duration: {duration_min_display}:{duration_sec_display:02d}...")
        
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
    duration_range = input("Enter the duration range in minutes (e.g., 2-4 or 3-5): ")
    try:
        # Parse the range format "min-max"
        range_parts = duration_range.split('-')
        if len(range_parts) != 2:
            raise ValueError
        min_duration = int(range_parts[0].strip())
        max_duration = int(range_parts[1].strip())
        
        if min_duration <= 0 or max_duration <= 0 or min_duration > max_duration:
            raise ValueError
    except ValueError:
        print("❌ Invalid duration range. Please use format like '2-4' or '3-5'.")
    else:
        split_video_into_parts(video_location, start_at, min_duration_min=min_duration, max_duration_min=max_duration)
