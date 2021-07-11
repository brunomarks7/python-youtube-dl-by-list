import os

with open("videos.txt") as file_in:
    for line in file_in:
        os.system("youtube-dl -f 22 -o %\(title\)s.f%\(format_id\)s.%\(ext\)s http://www.youtube.com/watch?v={line}".format(line=line))
    print("Download finish!")
