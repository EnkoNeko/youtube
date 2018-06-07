# Manages stage 2 of youtubeBot

grep -o 'v=.*' allURL.txt | cut -f2 -d"="| tr '\n' ',' > allCSV.csv    # Splits the selected URLs up into a CSV file
cut -d',' -f1-49 allCSV.csv > csv1.txt && cut -d',' -f50-99 \
allCSV.csv > csv2.txt && cut -d',' -f100-149 allCSV.csv > csv3.txt    # Splits the CSV file into smaller text files
python3 sep.py    # Runs the final program, sep.py
