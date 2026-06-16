# SmartClip-Automator

Effortlessly split video files into manageable clips of your desired duration. Perfect for content creators, video editors, and anyone who needs to break down long videos into smaller segments.

## Features

✨ **Easy-to-Use Interface** - Simple command-line prompts to get started  
⏱️ **Flexible Duration Control** - Split videos into custom-length segments  
🎬 **Multiple Format Support** - Works with MP4 and other video formats  
📁 **Organized Output** - Automatically creates an output folder for all clips  
🔧 **Time Format Support** - Accepts HH:MM:SS format for precise start times  
✅ **Input Validation** - Ensures correct time and duration formats

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

3. **Split duration** - Length of each clip in minutes
   ```
   Enter the split duration in minutes (whole number): 4
   ```

The script will automatically create an `Output_Parts` folder and save all clips with names like `Part_1.mp4`, `Part_2.mp4`, etc.

## Example

```bash
Video file path: D:\Videos\long_podcast.mp4
Start time: 00:10:00
Split duration: 5 minutes
```

This will create 5-minute clips starting from the 10-minute mark of `long_podcast.mp4`.

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
- Split duration must be a positive whole number
- Make sure the video file path is correct and the file is accessible
- The output folder will be created in the same directory where you run the script

## Author

**Lakshitha Madumal**

## License

This project is open-source and available under the MIT License.

## Troubleshooting

**"Video file not found"** - Check that the file path is correct and the file exists

**"Invalid time format"** - Use HH:MM:SS format (e.g., 01:30:45 for 1 hour, 30 minutes, 45 seconds)

**"Invalid duration"** - Enter a positive whole number for the duration in minutes

**FFmpeg errors** - Make sure FFmpeg is installed and added to your system PATH

## Support

For issues, feature requests, or contributions, please visit the [GitHub repository](https://github.com/lakshithamadumal/SmartClip-Automator).
