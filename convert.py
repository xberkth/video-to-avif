import sys
import os
import subprocess
import shutil

def get_framerate(input_file):
    """Extracts the original framerate of the video."""
    try:
        result = subprocess.run([
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=r_frame_rate",
            "-of", "default=noprint_wrappers=1:nokey=1", input_file
        ], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        print("Warning: Could not detect framerate, defaulting to 30fps.")
        return "30"

def convert_to_avif(input_file):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    temp_dir = "temp_frames"
    y4m_file = "temp_output.y4m"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # Extract to PNGs
        print(f"Step 1: Extracting frames from '{input_file}'")
        subprocess.run([
            "ffmpeg", "-y", "-vcodec", "libvpx-vp9", "-i", input_file,
            os.path.join(temp_dir, "%04d.png")
        ], check=True)

        fps = get_framerate(input_file)
        
        # Compile PNGs into a raw Y4M sequence with an alpha channel
        print("Step 2: Compiling raw video with alpha track")
        subprocess.run([
            "ffmpeg", "-y", 
            "-framerate", fps, 
            "-i", os.path.join(temp_dir, "%04d.png"),
            "-pix_fmt", "yuva444p",
            "-strict", "-1",
            y4m_file
        ], check=True)

        # Encoder for final compression
        print("Step 3: Encoding final AVIF with avifenc")
        subprocess.run([
            "avifenc", y4m_file, "animated.avif"
        ], check=True)

        print("Conversion completed successfully: 'animated.avif' created")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during execution: {e}")
    except Exception as e:
         print(f"An unexpected error occurred: {e}")
    finally:
        # Cleanup
        print("Cleaning up temporary files")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        if os.path.exists(y4m_file):
            os.remove(y4m_file)
        print("Temporary files removed")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert.py <your_file_name.webm>\nMake sure to have ffmpeg and avifenc in the same directory or added to your PATH")
    else:
        convert_to_avif(sys.argv[1])