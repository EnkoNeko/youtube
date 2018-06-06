# Takes in an input file of youtube searches, then outputs the URLs to one file, and the URLs & video title to another file

import requests as re
from bs4 import BeautifulSoup
import codecs as codecs

with open('input3.txt') as infile:
    searchtext = infile.read()

for searchquery in searchtext.splitlines():
    html = re.get("https://www.youtube.com/results?search_query=" + searchquery + "+hq+audio").text
    soup = BeautifulSoup(html, "lxml")
    video = soup.find(attrs={'class':'yt-uix-tile-link'})

      # Print URL and save to out1.txt
    print('https://www.youtube.com{}'.format(video["href"]))
    with open("out1.txt", 'a') as f:
        f.write('https://www.youtube.com{}\n'.format(video["href"]))

      # Print URL --- title, and save to out2.txt
    print('https://www.youtube.com{}'.format(video["href"]), " ---  {}".format(video["title"]))
    with open("out2.txt", 'a') as f:
        f.write('https://www.youtube.com{}'.format(video["href"]))
        f.write(' ---  {}\n'.format(video["title"]))
