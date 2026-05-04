# Audio Speed Editor Desktop

A lightweight desktop application for changing the playback speed of audio files without affecting pitch. Built with Python and PySide6.

## Features

- **Adjust Audio Speed**: Change playback speed from 0.5x to 2.0x without altering pitch
- **Multiple Format Support**: Works with MP3, WAV, AAC, and M4A audio files
- **Simple GUI**: Clean and intuitive user interface for easy operation
- **Batch-Ready**: Process one file at a time with clear output paths
- **Cross-Platform**: Runs on Windows, macOS, and Linux

## Requirements

- Python 3.13 or higher
- FFmpeg (required for audio processing)
- PySide6 6.10.2 or higher

### Installing FFmpeg

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Using Winget
winget install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

### Installing uv

This project uses [uv](https://github.com/astral-sh/uv) for dependency management. Install it from the [official documentation](https://docs.astral.sh/uv/getting-started/installation/).

## Quick Start (Bundled Version)

If you prefer not to install Python dependencies, you can download the pre-built executable:

1. **Download the executable:**
   - Download directly from the `dist` folder after cloning the repository or download it directly from github

2. **Run the application:**
   - Simply double-click `AudioSpeedEditor.exe` on Windows
   - No Python installation or additional setup required

> **Note:** The bundled version requires FFmpeg to be installed on your system. Follow the FFmpeg installation instructions above.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/brunomvilela/Audio-Speed-Editor-Desktop.git
   cd Audio-Speed-Editor-Desktop
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   uv sync
   ```

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **In the GUI:**
   - Click "Selecionar Áudio" (Select Audio) to choose an audio file
   - Set the desired speed (0.5 = half speed, 2.0 = double speed)
   - Click "Processar" (Process) to generate the speed-adjusted audio file
   - The output file will be saved in the same directory as the input file with `_speed_[value].mp3` appended to the filename

## Building your own Executable

To create a standalone executable for distribution:

```bash
# Install all dependencies (including dev)
uv sync

# Build the executable
uv run pyinstaller --onefile --windowed --icon=assets/main_icon.ico --add-data "assets;assets" --name "AudioSpeedEditor"  main.py
```

The executable will be available in the `dist/` directory.

## Project Structure

```
Audio-Speed-Editor-Desktop/
├── main.py                 # Application entry point
├── pyproject.toml         # Project configuration and dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── assets/                # Application icons and resources
├── ui/
│   └── mainWindow.py      # GUI implementation (PySide6)
├── services/
│   └── audioProcess.py    # Audio processing logic (FFmpeg wrapper)
├── utils/
│   └── paths.py           # Path utility functions
└── build/                 # PyInstaller build output
```

## How It Works

The application uses FFmpeg's `atempo` audio filter to change playback speed while maintaining pitch quality. This is different from simple time-stretching or pitch-shifting, providing natural-sounding results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Bruno Vilela Batista

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.