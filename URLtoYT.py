# Converts the URLs into a YT playlist

import requests

f = open('csv1.txt','r')
newf = open('playlist.txt','w')
lines = f.readlines()
newf.write("http://www.youtube.com/watch_videos?video_ids=")
for line in lines:
    newf.write(line)
newf.close()
f.close()

with open ("playlist.txt", "r") as playl:
    search=playl.readline()
r = requests.get(search.strip())
id = r.url.split("=")[2]
full = "https://www.youtube.com/playlist?list={}&disable_polymer=true".format(id)
print(full, "\nIf multiple csv.txt files, edit file number in \"URLtoYT.py\", and run from there")
