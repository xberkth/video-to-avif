# Video to AVIF Converter

Python script that converts video files (like `.mp4`, `.webm`, `.mkv`, `.mov`, etc.) into high-quality animated `.avif` files while preserving the alpha channel (transparency). 

## Prerequisites (Windows Only)
To run this script, you need two command-line tools installed and accessible on your Windows machine:

1. **[FFmpeg](https://ffmpeg.org/download.html):** The official FFmpeg.
   * Go to Get packages & executable files > Windows > Windows builds from gyan.dev, then on section `release builds` download `ffmpeg-release-essentials.zip` or use this link -> [direct-download](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip), and extract `ffmpeg.exe`.
   * Place it either in the same folder as this script, or add it to your Windows System PATH.
2. **[avifenc (libavif)](https://github.com/AOMediaCodec/libavif/releases):** The official AVIF encoder.
   * Go to the GitHub releases page, download the latest `windows-artifacts.zip`, and extract `avifenc.exe`. 
   * Place it either in the same folder as this script, or add it to your Windows System PATH.

## Usage
1. Make sure to have the prerequisites installed.
2. Clone this repository or [download](https://github.com/xberkth/video-to-avif/releases) the `convert.py` script.
3. Open Command Prompt or PowerShell in the directory containing the script.
4. Run the script and pass your input video file as an argument:

```cmd
python convert.py your_video.webm
