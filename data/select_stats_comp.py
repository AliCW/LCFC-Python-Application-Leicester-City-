import subprocess
from pathlib import Path

raw_path = str(Path(__file__).resolve().parent) #<--takes the raw path
double_dash = str('\\')

premiership1 = ('premier league')
premiership2 = ('pl')
fa1 = ('fa cup')
fa2 = ('f.a. cup')
fa3 = ('fa')
carab1 = ('carabao cup')
carab2 = ('cc')

def syntax_fail_loop():
    print('Incorrect syntax, try once more')
    select_stats()

def select_stats():
    answer00 = input('\nEnter the desired competition or its initials for statistics\n'
                     'Premier League (PL) / FA Cup (FA) / Carabao Cup (CC)\n').lower()
    if (answer00 == premiership1) or (answer00 == premiership2):
        subprocess.call(['python', raw_path + double_dash + 'current_player_stats.py'])
    if (answer00 == fa1) or (answer00 == fa2) or (answer00 == fa3):
        subprocess.call(['python', raw_path + double_dash + 'current_player_stats_fa_cup.py'])
    if (answer00 == carab1) or (answer00 == carab2):
        subprocess.call(['python', raw_path + double_dash + 'current_player_stats_league_cup.py'])
    else: syntax_fail_loop()

select_stats()