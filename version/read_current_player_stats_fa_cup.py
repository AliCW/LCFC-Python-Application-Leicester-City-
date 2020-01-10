#<--reads the first line of the file and caches the number to text file
from pathlib import Path

raw_path = str(Path(__file__).resolve().parent) #<--takes the raw path
data_path = str('\\data\\')

read_file = open(raw_path.rstrip('version') + data_path + 'current_player_stats_fa_cup.py') #<--takes /version/ out of the path so it can find run.py
for v, line in enumerate(read_file):
    if v == 0: #<-finds the first line (this should always contain the version number
        version_string = line
        print(version_string[2:7]) #<---removes some of the unnecessary characters so the output can be floated