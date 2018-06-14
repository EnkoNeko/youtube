# Flow  
List of YouTube search queries in input.txt    
search.py finds on YT, outputs the URLs to out1.txt and the URLs & Video title to out2.txt

copy.py copies unwanted URLs to trims.txt  
del.py deletes the original unwanted URLs  

Good video URLs in urls.txt  
grep.sh trims off urls.txt video IDs into allCSV.csv, separates further into smaller txt files and runs URLtoYT.py (streamline this)  
URLtoYT.py converts the ID chunks into a playlist and prints playlist ID  


# Contents  
URLtoYT.py - Converts selected URLs into a YT playlist    
grep.sh - Initialises and manages the 2nd stage    
search.py - Takes in queries, spits out URLs & titles    
copy.py - Copies unwanted URLs to a separate file for later  
del.py - Compares the wanted and unwanted URLs, deletes the duplicates from the wanted  

urls.txt - Necessary text file, holds full URLs  

# To do  
search.py -> out1.txt & out2.txt (search.py could output to one text file, then regex the URL)  
Combine copy.py and del.py to form cull.py  
grep.sh - skip allCSV.csv? Straight from urls.txt to smaller ID chunks    
grep.sh - make grep.sh manage all programs?    
URLtoYT.py - clean this code up  


Maybe -  
Initial conversion from Spotify playlist?  
Downloading the YT playlist?  
