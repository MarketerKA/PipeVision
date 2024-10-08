
# Telegram Video Processing Bot

## Project Overview
This project is a **Telegram bot** built with `aiogram` that allows users to send video files to the bot, which processes them using **OpenCV** and adds effects such as grayscale, mirroring, and resizing. Once processed, the bot combines the original audio with the modified video using **moviepy** and sends the final video back to the user.

## Features
- Users can upload videos directly to the bot.
- The video is processed with several effects:
  - **Grayscale conversion**: Converts the video to black-and-white.
  - **Mirroring**: Flips the video horizontally.
  - **Resizing**: Resizes the video to 640x480 resolution.
- After processing, the original audio is restored to the video.
- The final video (with effects and audio) is sent back to the user.
  
## Technologies Used
- **Python**: Core language for bot and video processing.
- **aiogram**: Framework for building Telegram bots.
- **OpenCV**: Handles frame-by-frame video processing.
- **moviepy**: Combines the processed video with the original audio.
- **Threading**: Used to handle video processing in parallel.

## Project Structure
```
/project-directory
├── bot.py               # Contains the Telegram bot logic
├── video_processor.py    # Contains video processing pipeline and audio merging logic
├── requirements.txt      # Lists project dependencies
└── README.md             # Documentation for the project
```

## How It Works
1. **Start Interaction**:
   - The bot greets the user and asks them to send a video.
2. **Processing Pipeline**:
   - The video is downloaded.
   - Several effects are applied:
     - Grayscale
     - Mirroring
     - Resizing
   - The processed video is saved temporarily.
3. **Audio Merging**:
   - The original audio from the uploaded video is extracted.
   - The processed video frames are combined with the original audio.
4. **Final Output**:
   - The final video (with both processed frames and audio) is sent back to the user.
   
## Setup Instructions

### 1. Clone the repository
   ```bash
   git clone https://github.com/your-repo/telegram-video-bot.git
   cd telegram-video-bot
   ```

### 2. Set up a virtual environment
   It is recommended to use a virtual environment for dependency management.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scriptsctivate
   ```

### 3. Install dependencies
   Install the required dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Set up the Telegram bot
   - Get your Telegram bot token by creating a bot using [BotFather](https://t.me/BotFather).
   - Replace the placeholder `API_TOKEN` in `bot.py` with your bot token.

### 5. Run the bot
   ```bash
   python bot.py
   ```

## Usage
1. Start a chat with the bot on Telegram.
2. Send a video file to the bot.
3. The bot will process the video and apply the effects (grayscale, mirror, resize).
4. The bot will send the processed video with the original audio back to you.

## Dependencies
This project requires the following Python packages, which are listed in `requirements.txt`:
- `aiogram`
- `opencv-python`
- `moviepy`
- `numpy`

You can install all dependencies with:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributing
Feel free to fork this project, submit pull requests, or open issues if you have any suggestions or find any bugs.

---

**Happy Coding!**
