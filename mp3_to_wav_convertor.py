import os
import sys
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    """Convert an MP3 file to a WAV file."""
    audio = AudioSegment.from_file(mp3_path, format="mp3")
    audio.export(wav_path, format="wav")

def main(mp3_folder, wav_folder):
    """Convert all MP3 files in the given folder to WAV files in the output folder."""
    # Make sure the output folder exists
    os.makedirs(wav_folder, exist_ok=True)

    # Get a list of all the MP3 files in the input folder
    mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]

    # Convert each MP3 file to a WAV file and save it in the output folder
    for mp3_file in mp3_files:
        mp3_path = os.path.join(mp3_folder, mp3_file)
        wav_file = mp3_file[:-4] + ".wav"  # replace ".mp3" with ".wav"
        wav_path = os.path.join(wav_folder, wav_file)
        print(f"Converting {mp3_path} to {wav_path}")
        convert_mp3_to_wav(mp3_path, wav_path)

if __name__ == "__main__":
    # Get the folder paths
    mp3_folder = input("Enter the MP3 files folder: ")
    wav_folder = input("Enter the destination folder for WAV files: ")
    
    # Call the main function
    main(mp3_folder, wav_folder)