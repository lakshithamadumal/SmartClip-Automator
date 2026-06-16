# SmartClip-Automator

Effortlessly split video files into manageable clips of your desired duration. Perfect for content creators, video editors, and anyone who needs to break down long videos into smaller segments.

## Features

✨ **Easy-to-Use Interface** - Simple command-line prompts to get started  
⏱️ **Random Duration Control** - Specify a range (e.g., 2-4 min) and each clip gets a random duration  
🎬 **Multiple Format Support** - Works with MP4 and other video formats  
📁 **Organized Output** - Automatically creates an output folder for all clips  
🔧 **Time Format Support** - Accepts HH:MM:SS format for precise start times  
✅ **Input Validation** - Ensures correct time and duration formats  
🛡️ **Spam-Prevention Ready** - Random durations help avoid platform spam detection algorithms

## Requirements

- Python 3.7 or higher
- MoviePy library
- FFmpeg (required by MoviePy)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshithamadumal/SmartClip-Automator.git
   cd SmartClip-Automator
   ```

2. **Install required Python packages:**
   ```bash
   pip install moviepy
   ```

3. **Install FFmpeg:**
   - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use `choco install ffmpeg`
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt-get install ffmpeg`

## Usage

Run the script from the command line:

```bash
python video_splitter.py
```

The script will prompt you for:

1. **Video file path** - Full path to your video file
   ```
   Enter the video file path: C:\Videos\my_video.mp4
   ```

2. **Start time** - When to begin splitting (HH:MM:SS format)
   ```
   Enter the start time to split from (HH:MM:SS): 00:05:30
   ```

3. **Duration range** - Length range for each clip in minutes (format: min-max)
   ```
   Enter the duration range in minutes (e.g., 2-4 or 3-5): 3-5
   ```

Each part will be automatically cut with a **random duration within the specified range** to avoid spam detection patterns on social media platforms like Facebook.

The script will automatically create an `Output_Parts` folder and save all clips with names like `Part_1.mp4`, `Part_2.mp4`, etc.

### Random Duration Feature

This tool uses **random durations for each clip** within your specified range, including random seconds. For example:
- **Input:** Duration range 6-7 minutes
- **Output:**
  - Part_1: 6:05 (6 minutes 5 seconds)
  - Part_2: 6:09 (6 minutes 9 seconds)
  - Part_3: 6:14 (6 minutes 14 seconds)
  - Part_4: 6:47 (6 minutes 47 seconds)

This creates unique durations for each clip (with seconds ranging 0-59 within the minute range), helping them pass platform algorithms and reducing spam flags on social media.

## Example

```bash
Video file path: D:\Videos\long_podcast.mp4
Start time: 00:10:00
Duration range: 6-7 minutes
```

This will create clips with random durations between 6-7 minutes (with random seconds 0-59), starting from the 10-minute mark of `long_podcast.mp4`.

**Sample output:**
- Part_1.mp4: 6:15
- Part_2.mp4: 6:52
- Part_3.mp4: 7:03
- Part_4.mp4: 6:28

## Output Structure

```
Output_Parts/
├── Part_1.mp4
├── Part_2.mp4
├── Part_3.mp4
└── Part_4.mp4
```

## Notes

- The start time must be earlier than the video duration
- Duration range must be in format "min-max" (e.g., 2-4 or 3-5) where min ≤ max
- Each part will have a random duration within the specified range
- Random durations help prevent platform spam detection when uploading to social media
- Make sure the video file path is correct and the file is accessible
- The output folder will be created in the same directory where you run the script

## Author

**Lakshitha Madumal**

## License

This project is open-source and available under the MIT License.

## Troubleshooting

**"Video file not found"** - Check that the file path is correct and the file exists

**"Invalid time format"** - Use HH:MM:SS format (e.g., 01:30:45 for 1 hour, 30 minutes, 45 seconds)

**"Invalid duration range"** - Use format "min-max" like "2-4" or "3-5", where minimum ≤ maximum

**FFmpeg errors** - Make sure FFmpeg is installed and added to your system PATH

## Support

For issues, feature requests, or contributions, please visit the [GitHub repository](https://github.com/lakshithamadumal/SmartClip-Automator).
