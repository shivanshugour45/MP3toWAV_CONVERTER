# MP3 to WAV Converter

This is a simple Python script that allows you to convert MP3 files to WAV files. It utilizes the `pydub` library for audio file manipulation.

## Prerequisites

Before using this script, make sure you have the following installed:

- Python 3.x
- `pydub` library

You also need to have **FFmpeg** installed on your system. FFmpeg is a command-line tool used for handling multimedia data, including audio and video conversion. The `pydub` library relies on FFmpeg for audio file format conversion.

## Installation

### FFmpeg

#### Windows

1. Visit the official FFmpeg website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

2. Scroll down to the "Windows Builds" section and click on the link that corresponds to your system architecture (32-bit or 64-bit).

3. Download the ZIP archive containing the FFmpeg binaries.

4. Extract the contents of the ZIP archive to a directory on your system. For example, you can extract it to `C:\ffmpeg`.

5. Add the FFmpeg executable directory to your system's **Path** environment variable. Here's how:

   - Open the **Control Panel** and go to **System and Security** → **System** → **Advanced system settings**.
   - Click on the **Environment Variables** button.
   - In the **System variables** section, select the **Path** variable and click on **Edit**.
   - Click on **New** and enter the path to the FFmpeg executable directory (e.g., `C:\ffmpeg\bin`).
   - Click **OK** to save the changes.

6. Open a new command prompt window and type `ffmpeg`. If everything is set up correctly, you should see the FFmpeg version information printed in the console.

#### macOS

1. Open Terminal.

2. Install FFmpeg using Homebrew by running the following command:

   ```
   brew install ffmpeg
   ```

3. Wait for the installation to complete. Once finished, you should have FFmpeg installed on your system.

4. To verify the installation, type `ffmpeg` in the terminal and press Enter. You should see the FFmpeg version information displayed.

#### Linux

1. Open a terminal.

2. Install FFmpeg using the package manager for your Linux distribution. The package name might vary depending on the distribution. Here are the commands for some popular distributions:

   - **Ubuntu/Debian**:

     ```
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```

   - **Fedora/RHEL**:

     ```
     sudo dnf install ffmpeg
     ```

   - **Arch Linux**:

     ```
     sudo pacman -S ffmpeg
     ```

3. Wait for the installation to complete. Once finished, you should have FFmpeg installed on your system.

4. To verify the installation, type `ffmpeg` in the terminal and press Enter. You should see the FFmpeg version information displayed.

### Python Packages

To install the required Python packages, use the following command:

```
pip install pydub
```

## Usage

1. Clone the repository or download the `mp3_to_wav_converter.py` file.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```
   python mp3_to_wav_converter.py
   ```

4. The script will prompt you to enter the folder path containing the MP3 files and the destination folder path for the converted WAV files. Provide the required paths and press Enter.

5. The script will convert all the MP3 files in the specified folder to WAV files and save them in the destination folder.

6. The conversion progress will be displayed in the terminal.

7. Once the conversion is complete, you can find the converted WAV files in the specified destination folder.

## Example

Here's an example usage of the script:

```
Enter the MP3 files folder: /path/to/mp3_folder
Enter the destination folder for WAV files: /path/to/wav_folder
Converting /path/to/mp3_folder/file1.mp3 to /path/to/wav_folder/file1.wav
Converting /path/to/mp3_folder/file2.mp3 to /path/to/wav_folder/file2.wav
Converting /path/to/mp3_folder/file3.mp3 to /path/to/wav_folder/file3.wav
Conversion completed successfully.
```

## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [pydub](https://github.com/jiaaro/pydub) - A simple and easy-to-use library for audio file manipulation in Python.
