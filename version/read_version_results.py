#<--reads the first line of the file and caches the number to text file
from pathlib import Path

raw_path = str(Path().absolute()) #<--takes the raw path
data_path = str('data\\')
#print(raw_path.strip('version') + data_path)

read_file = open(raw_path.strip('version') + data_path + 'current_results.py') #<--takes /version/ out of the path so it can find run.py
for v, line in enumerate(read_file):
    if v == 0: #<-finds the first line (this should always contain the version number
        version_string = line
        print(version_string.replace('#v', '')) #<---removes some of the unnecessary characters so the output can be floated