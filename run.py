#v0.05
import subprocess
import html
import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitCondition
from bs4 import BeautifulSoup as BeautifulSoup

statistics = str('stats')
command = str('commands')
fixtures = str('fixtures')
update_data = str('update data')
update_run_file = str('update launcher')
results = str('scores')
rst1 = str('reset')
clean = str('clean')
restart = str('restart')
fx_version = str('fixture version') #version for fixture
pl_version = str('player version') #version for player stats
rs_version = str('results version') #version for results
run_version = str('run version') #version for run.py
yes = str('y')
no = str('n')
shut_down = str('exit')

base_path = os.environ['IDEA_INITIAL_DIRECTORY']
data_path = str('\\data\\')
version_path = str('\\version\\')
update_path = str('\\update\\')
old_path = str('\\old\\')
double_dash = str('\\')

try:
    open_run_version = open(base_path + version_path + 'run_version.py')
    open_run_version.close()
    current_run_version = subprocess.check_output(['python', base_path + version_path + 'run_version.py'])
except IOError:
    print('No version file found for run.py, running the update process...')
    subprocess.call(['python', base_path + update_path + 'run_update.py'])#<----Runs the external update script
    current_run_version = subprocess.check_output(['python', base_path + version_path + 'run_version.py'])
try:
    open_run_update = open(base_path + update_path + 'run_update.py')
    open_run_update.close()
except IOError:
    print('No run_update.py file found, obtaining one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/update/run_update.py')
    WebDriverWait(browser, 10)
    run_update_raw = browser.page_source
    run_update_parsed = html.unescape(run_update_raw)
    run_update_soup = BeautifulSoup(run_update_parsed, features='html.parser')
    run_update_final = run_update_soup.pre.string
    run_update_create = open(base_path + update_path + 'run_update.py', 'w+')
    run_update_create.write(run_update_final)
    run_update_create.close()
    browser.close()
try: #<-------------Player Statistic Version File
    open_player_stats_version = open(base_path + version_path + 'current_player_stats_version.py') #<--Checks the presence of the file
    open_player_stats_version.close() #if it finds it, the program checks the version output
    player_stats_current_version = subprocess.check_output(['python', base_path + version_path + 'current_player_stats_version.py'])
except IOError: #<--Run this update process if no file is found - functions the same as the update mechanism
    print('No version file found for player statistics, creating a new one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/current_player_stats_version.py')
    WebDriverWait(browser, 10)#<-----------------------------------improve this to speed up the process!!!
    new_player_version_raw = browser.page_source
    new_player_version_parsed = html.unescape(new_player_version_raw)
    new_player_version_soup = BeautifulSoup(new_player_version_parsed, features='html.parser')
    new_player_version_final = new_player_version_soup.pre.string
    player_version_create = open(base_path + version_path + 'current_player_stats_version.py', 'w+')
    player_version_create.write(new_player_version_final)
    player_version_create.close()
    browser.close()
    player_stats_current_version = subprocess.check_output(['python', base_path + version_path + 'current_player_stats_version.py'])
try: #<-------------Player Statistic Data File
    open_player_stat = open(base_path + data_path + 'current_player_stats.py')
    open_player_stat.close()
except IOError:
    print('No player statistic file found, creating a new one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/data/current_player_stats.py')
    WebDriverWait(browser, 10)
    new_player_stats_raw = browser.page_source
    new_player_stats_parsed = html.unescape(new_player_stats_raw)
    new_player_stats_soup = BeautifulSoup(new_player_stats_parsed, features='html.parser')
    new_player_stats_final = new_player_stats_soup.pre.string
    player_stats_create = open(base_path + data_path + 'current_player_stats.py', 'w+')
    player_stats_create.write(new_player_stats_final)
    player_stats_create.close()
    browser.close()
try: #<-------------Fixture Version File
    open_fixture_list_version = open(base_path + version_path + 'current_fixture_version.py')
    open_fixture_list_version.close()
    fixture_list_current_version = subprocess.check_output(['python', base_path + version_path + 'current_fixture_version.py'])
except IOError:
    print('No version file found for fixture listings, creating a new one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/current_fixture_version.py')
    WebDriverWait(browser, 10)
    new_fixture_version_raw = browser.page_source
    new_fixture_version_parsed = html.unescape(new_fixture_version_raw)
    new_fixture_version_soup = BeautifulSoup(new_fixture_version_parsed, features='html.parser')
    new_fixture_version_final = new_fixture_version_soup.pre.string
    fixture_version_create = open(base_path + version_path + 'current_fixture_version.py', 'w+')
    fixture_version_create.write(new_fixture_version_final)
    fixture_version_create.close()
    browser.close()
    fixture_list_current_version = subprocess.check_output(['python', base_path + version_path + 'current_fixture_version.py'])
try: #<-------------Fixture Data File
    open_fixture_list = open(base_path + data_path + 'current_fixture_list.py')
    open_fixture_list.close()
except IOError:
    print('No fixture listing file found, creating a new one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/data/current_fixture_list.py')
    WebDriverWait(browser, 10)
    new_fixture_list_raw = browser.page_source
    new_fixture_list_parsed = html.unescape(new_fixture_list_raw)
    new_fixture_list_soup = BeautifulSoup(new_fixture_list_parsed, features='html.parser')
    new_fixture_list_final = new_fixture_list_soup.pre.string
    fixture_list_create = open(base_path + data_path + 'current_fixture_list.py', 'w+')
    fixture_list_create.write(new_fixture_list_final)
    fixture_list_create.close()
    browser.close()
try: #<-------------Results Version File
    open_results_version = open(base_path + version_path + 'current_results_version.py')
    open_results_version.close()
    results_list_current_version = subprocess.check_output(['python', base_path + version_path + 'current_results_version.py'])
except IOError:
    print('No version file found for latest results, creating a new one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/current_results_version.py')
    WebDriverWait(browser, 10)
    new_results_version_raw = browser.page_source
    new_results_version_parsed = html.unescape(new_results_version_raw)
    new_results_version_soup = BeautifulSoup(new_results_version_parsed, features='html.parser')
    new_results_version_final = new_results_version_soup.pre.string
    results_version_create = open(base_path + version_path + 'current_results_version.py', 'w+')
    results_version_create.write(new_results_version_final)
    results_version_create.close()
    browser.close()
    results_list_current_version = subprocess.check_output(['python', 'current_results_version.py'])
try: #<-------------Results Data File
    open_results_list = open(base_path + data_path + 'current_results.py')
    open_results_list.close()
except IOError:
    print('No results file found, creating one now.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/data/current_results.py')
    WebDriverWait(browser, 10)
    new_results_list_raw = browser.page_source
    new_results_list_parsed = html.unescape(new_results_list_raw)
    new_results_list_soup = BeautifulSoup(new_results_list_parsed, features='html.parser')
    new_results_list_final = new_results_list_soup.pre.string
    results_list_create = open(base_path + data_path +'current_results.py', 'w+')
    results_list_create.write(new_results_list_final)
    results_list_create.close()
    browser.close()

def update_tool():
    print('Started\n')
    if os.path.exists(base_path + old_path):
        print('Existing .old folder found')
    if not os.path.exists(base_path + old_path):
        print('Creating .old folder...')
        os.makedirs(base_path + old_path)
    print('Checking for the latest statistic files')
    options = Options() #define browser options
    options.headless = True #set options to headless
    browser = webdriver.Firefox(options=options) #opens a headless firefox named "browser"
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/update/update_table.txt') #browser is sent to overall table - this file must always contain the latest version number
    print('Internet loaded')
    WebDriverWait(browser, 10)#.until(waitCondition.presence_of_element_located((By.id, '"player_update_version"')))
    update_list = browser.page_source
    escape_list = html.unescape(update_list)
    player_soup = BeautifulSoup(escape_list, features='html.parser')
    fixture_soup = BeautifulSoup(escape_list, features='html.parser')
    results_soup = BeautifulSoup(escape_list, features='html.parser')
    player_update_string = player_soup.main.string #takes the text out of the "main" section - IDed internally within the HTML page - PLAYER UPDATE SECTION
    fixture_update_string = fixture_soup.p.string #takes the version number from the "p" section
    results_update_string = results_soup.h1.string
    print('Latest Player Version: ' + player_update_string)
    print('Latest Fixture Version: ' + fixture_update_string)
    print('Latest Results Version: ' + results_update_string)
    if float(results_update_string) > float(results_list_current_version):
        print('\nResults list is out of date')
        results_list_update_query = input('\nWould you like to update LCFC results? Y / N\n')
        if results_list_update_query == yes:
            print('Working...')
            os.replace(base_path + version_path + 'current_results_version.py', base_path + old_path + 'current_results_version.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/current_results_version.py')
            latest_result_version_raw = browser.page_source
            latest_result_version_parsed = html.unescape(latest_result_version_raw)
            latest_result_version_soup = BeautifulSoup(latest_result_version_parsed, features='html.parser')
            latest_result_version_final = latest_result_version_soup.pre.string
            result_version_create = open(base_path + version_path + 'current_results_version.py', 'w+')
            result_version_create.write(latest_result_version_final)
            result_version_create.close()
            os.replace(base_path + data_path + 'current_results.py', base_path + old_path + 'current_results.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/data/current_results.py')
            latest_result_raw = browser.page_source
            latest_result_parsed = html.unescape(latest_result_raw)
            latest_result_soup = BeautifulSoup(latest_result_parsed, features='html.parser')
            latest_result_final = latest_result_soup.pre.string
            result_create = open(base_path + data_path + 'current_results.py', 'w+')
            result_create.write(latest_result_final)
            result_create.close()
        if results_list_update_query == no:
            print('Very Well...')
    if float(results_update_string) <= float(results_list_current_version):
        print('\nResults list is up to date!')
    if float(player_update_string) > float(player_stats_current_version): #compares internal file version with github file version
        print('\nPlayer statistics are out of date')
        player_stats_update_query = input('\nWould you like to update LCFC player statistics? Y / N\n')
        if player_stats_update_query == yes:
            print('Working...')
            os.replace(base_path + version_path + 'current_player_stats_version.py', base_path + old_path + 'current_player_stats_version.old.py') #Goalkeeper version code
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/current_player_stats_version.py')
            latest_player_stat_version_raw = browser.page_source
            latest_player_stat_version_parsed = html.unescape(latest_player_stat_version_raw)
            latest_player_stat_version_soup = BeautifulSoup(latest_player_stat_version_parsed, features='html.parser')
            latest_player_stat_version_final = latest_player_stat_version_soup.pre.string
            player_version_create = open(base_path + version_path + 'current_player_stats_version.py', 'w+')
            player_version_create.write(latest_player_stat_version_final)
            player_version_create.close()
            os.replace(base_path + data_path + 'current_player_stats.py', base_path + old_path + 'current_player_stats.old.py') #Goalkeeper statistic code
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/data/current_player_stats.py')
            latest_player_stats_raw = browser.page_source
            latest_player_stat_parsed = html.unescape(latest_player_stats_raw)
            latest_player_stat_soup = BeautifulSoup(latest_player_stat_parsed, features='html.parser')
            latest_player_stat_final = latest_player_stat_soup.pre.string
            player_stats_create = open(base_path + data_path + 'current_player_stats.py', 'w+')
            player_stats_create.write(latest_player_stat_final)
            player_stats_create.close()
        if player_stats_update_query == no:
            print('Very well...')
    if float(player_update_string) <= float(player_stats_current_version):
        print('\nPlayer statistic files are up to date!')
    if float(fixture_update_string) > float(fixture_list_current_version):
        print('Fixture list if out of date\n')
        fixture_update_query = input('Would you like to update LCFC fixtures? Y / N\n').lower()
        if fixture_update_query == yes:
            print('Working...')
            os.replace(base_path + version_path + 'current_fixture_version.py', base_path + old_path + 'current_fixture_version.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/current_fixture_version.py')
            latest_fixture_version_raw = browser.page_source
            latest_fixture_version_parsed = html.unescape(latest_fixture_version_raw)
            latest_fixture_version_soup = BeautifulSoup(latest_fixture_version_parsed, features='html.parser')
            latest_fixture_version_final = latest_fixture_version_soup.pre.string
            fixture_version_create = open(base_path + version_path + 'current_fixture_version.py', 'w+')
            fixture_version_create.write(latest_fixture_version_final)
            fixture_version_create.close()
            os.replace(base_path + data_path + 'current_fixture_list.py', base_path + old_path + 'current_fixture_list.old.py') #changes current name to .old - delete the .old file maybe within another script / function - MAY NEED AN OVERRIDE FUNCTION FOR THIS
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/data/current_fixture_list.py') #goes to the page with latest fixture file raw code
            latest_fixture_code_raw = browser.page_source #copies the raw code
            latest_fixture_code_parsed = html.unescape(latest_fixture_code_raw) #parses the code to retain symbolism
            latest_fixture_code_soup = BeautifulSoup(latest_fixture_code_parsed, features='html.parser')
            latest_fixture_code_final = latest_fixture_code_soup.pre.string
            fixture_page_create = open(base_path + data_path + 'current_fixture_list.py', 'w+') #creates the new fixture page
            fixture_page_create.write(latest_fixture_code_final) #writes the code to the new fixture page
            fixture_page_create.close() #closes the new fixture page
            browser.close()
        if fixture_update_query == no:
            print('Very well...')
            browser.close()
    if float(fixture_update_string) <= float(fixture_list_current_version):
        print('\nFixture list files are up to date!')
        browser.close()
    else: player_passed_close_page()
    startupquery00()

def player_passed_close_page():
    print('Update tool has completed')

def clean_old_files():
    print('Checking for .old files...')
    from os import path
    if os.path.exists(base_path + old_path):
        print('Existing .old folder found')
    if not os.path.exists(base_path + old_path):
        print('Creating .old folder...')
        os.makedirs(base_path + old_path)
    try:
        run_version_file = os.path.join(base_path + old_path + 'run_version.old.py')
        path.exists(run_version_file)
        os.remove(run_version_file)
        print('Run version file deleted')
    except IOError:
        print('No .old run version file found')
    try:
        run_file = os.path.join(base_path + old_path + 'run.old.py')
        path.exists(run_file)
        os.remove(run_file)
    except IOError:
        print('No .old run file found')
    try:
        fixture_version_file = os.path.join(base_path + old_path + 'current_fixture_version.old.py')
        path.exists(fixture_version_file)
        os.remove(fixture_version_file)
        print('Fixture version file deleted')
    except IOError:
        print('No .old fixture version files found') #<---Remove these statements??
    try:
        fixture_data_file = os.path.join(base_path + old_path + 'current_fixture_list.old.py')
        path.exists(fixture_data_file)
        os.remove(fixture_data_file)
        print('Fixture data file deleted')
    except IOError:
        print('No .old fixture data file found')
    try:
        player_version_file = os.path.join(base_path + old_path + 'current_player_stats_version.old.py')
        path.exists(player_version_file)
        os.remove(player_version_file)
        print('Player statistic version file deleted')
    except IOError:
        print('No .old player statistic version file found')
    try:
        player_data_file = os.path.join(base_path + old_path + 'current_player_stats.old.py')
        path.exists(player_data_file)
        os.remove(player_data_file)
        print('Player statistics data file deleted')
    except IOError:
        print('No .old player statistic data file found')
    try:
        results_version_file = os.path.join(base_path + old_path + 'current_results_version.old.py')
        path.exists(results_version_file)
        os.remove(results_version_file)
        print('Results version file deleted')
    except IOError:
        print('No .old results version file found')
    try:
        results_data_file = os.path.join(base_path + old_path + 'current_results.old.py')
        path.exists(results_data_file)
        os.remove(results_data_file)
        print('Results data file deleted')
    except IOError:
        print('No .old results data file found')

def startupquery00fail():
    print('Incorrect syntax, please try once more\n')
    startupquery00()

def startupquery00():
    startquery = input('\nType "stats" for player statistics.\nType "fixtures" for the fixture list.'
                       '\nType "commands" for a list of other features or "exit" to close the program.'
                       '\nType "scores" for the list of results in this years season.\n').lower()
    if (startquery == command): #lists available commands
        list_of_commands()
        startupquery00()
    if (startquery == fixtures):
        subprocess.call(['python', base_path + data_path + 'current_fixture_list.py'])
        startupquery00()
    if (startquery == statistics):
        subprocess.call(['python', base_path + data_path + 'current_player_stats.py'])
        startupquery00()
    if (startquery == results):
        subprocess.call(['python', base_path + data_path + 'current_results.py'])
        startupquery00()
    if (startquery == shut_down):
        sys.exit()
    else: startupquery00fail()

def list_of_commands():
    command_list = input('\nfixtures / stats / clean / restart\n'
                         'player/or/fixture/or/results/or/run version\n'
                         'update data/or/launcher\n'
                         '\nType "reset" to go back to the beginning\n').lower()
    if (command_list == update_data):
        update_tool()
    if (command_list == restart):
        subprocess.call(['python', 'run_restart.py'])#<-----restart function doest work yet
    if (command_list == clean):
        clean_old_files()
        list_of_commands()
    if (command_list == update_run_file):
        subprocess.call(['python', base_path + update_path + 'run_update.py'])
        list_of_commands()
    if (command_list == fixtures):
        subprocess.call(['python', base_path + data_path + 'current_fixture_list.py']) #downloads the new fixture list
        list_of_commands()
    if (command_list == statistics):
        subprocess.call(['python', base_path + data_path + 'current_player_stats.py'])
        list_of_commands()
    if (command_list == results):
        subprocess.call(['python', base_path + data_path + 'current_results.py'])
        list_of_commands()
    if (command_list == rst1):
        startupquery00()
    if (command_list == fx_version):
        print(float(fixture_list_current_version))
        list_of_commands()
    if (command_list == pl_version):
        print(float(player_stats_current_version))
        list_of_commands()
    if (command_list == rs_version):
        print(float(results_list_current_version))
        list_of_commands()
    if (command_list == run_version):
        print(float(current_run_version))
        list_of_commands()
    if (command_list == shut_down):
        sys.exit()
    else: list_of_commands_failed_syntax()

def list_of_commands_failed_syntax():
    print('\nUnknown command syntax\n')
    list_of_commands()

startupquery00()
