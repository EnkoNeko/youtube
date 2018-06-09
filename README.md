# Flow
1. List of YouTube search queries in input.txt
2. search.py finds on YT, outputs the URLs to out1.txt and the URLs & Video title to out2.txt
3. cull.py trims the bad videos for later consideration (Copying done, out2.txt deletion not)
4. Good video URLs in urls.txt
5. grep.sh trims off urls.txt video IDs into allCSV.csv, separates further into smaller txt files and runs URLtoYT.py (streamline this)
6. URLtoYT.py converts the ID chunks into a playlist and prints playlist ID


# Contents
URLtoYT.py - Converts selected URLs into a YT playlist  
grep.sh - Initialises and manages the 2nd stage  
search.py - Takes in queries, spits out URLs & titles  
cull.py - Trims unwanted URLs to a separate file for later

urls.txt - Necessary text file, holds full URLs

# To do
search.py -> out1.txt & out2.txt: could output to one text file, then regex the URL  
Culling - Compare differences between trims.txt and out2.txt, delete duplicates from out2.txt ([example](https://stackoverflow.com/questions/7537099/comparing-two-text-files-and-remove-duplicates-in-python))  
grep.sh - skip allCSV.csv? straight from urls.txt to smaller ID chunks  
        - make grep.sh manage all programs?  
URLtoYT.py - clean this code up


Maybe -  
Initial conversion from Spotify playlist?  
Downloading the YT playlist?



Initially transferred to Github 6/06/2018
