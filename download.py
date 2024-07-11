import os

with open("videos.txt") as file_in:
    for line in file_in:
        os.system(f"yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 -o '%(title)s.%(ext)s' -- {line.strip()}")
    print("Download finished!")
