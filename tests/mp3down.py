import os
import sys
import subprocess

def download_audio(url, output_name):
    try:
        output_path = os.path.join("/home/apshv/Music/Chalgata", f"{output_name}.mp3")
        # output_path = "/home/apshv/Music/"
        subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "--add-metadata", "--embed-thumbnail", "-o", output_path, url], check=True)
        print("Audio downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print("Error downloading audio:", e)

def get_download_dir():
    return os.getcwd()

def get_video_title(url):
    try:
        result = subprocess.run(["yt-dlp", "--get-title", url], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        print("Error getting video title:", e)
        sys.exit(1)

def main(url, output_name):
    # if len(sys.argv) < 3:
    #     print("Usage: python download_audio.py <youtube_url> <output_name>")
    #     sys.exit(1)

    # url = sys.argv[1]
    # output_name = sys.argv[2]

    download_audio(url, output_name)
    
def forLoop(playlist):
    for vids in playlist:
        for atrs in vids:
            download_audio(atrs[1], atrs[0])

if __name__ == "__main__":
    main()