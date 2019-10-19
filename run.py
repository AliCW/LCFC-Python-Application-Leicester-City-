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
update = str('update')
rst1 = str('reset')
fx_version = str('fixture version') #version for fixture
pl_version = str('player version') #version for player stats
yes = str('y')
no = str('n')
shut_down = str('exit')

#<-----Current version number scripts
player_stats_current_version = subprocess.check_output(['python', 'current_player_stats_version.py'])
fixture_list_current_version = subprocess.check_output(['python', 'current_fixture_version.py']) #runs process on version file to gain the version number
                                            #need to use check_output in order to float the value for comparison (what didnt work?)
def startuppage():
    print('Started\n')
    print('Checking for the latest statistic files')
    options = Options() #define browser options
    options.headless = True #set options to headless
    browser = webdriver.Firefox(options=options) #opens a headless firefox named "browser"
    browser.get('https://raw.githubusercontent.com/AliCW/Test/master/update_table.txt') #browser is sent to overall table - this file must always contain the latest version number
    print('Internet loaded')
    WebDriverWait(browser, 10)#.until(waitCondition.presence_of_element_located((By.id, '"player_update_version"')))
    update_list = browser.page_source
    escape_list = html.unescape(update_list)
    player_soup = BeautifulSoup(escape_list, features='html.parser')
    fixture_soup = BeautifulSoup(escape_list, features='html.parser')
    player_update_string = player_soup.main.string #takes the text out of the <main> section - IDed internally within the HTML page - PLAYER UPDATE SECTION
    fixture_update_string = fixture_soup.p.string #takes the version number from the <p> section
    print('Latest player version: ' + player_update_string)
    print('Latest fixture version: ' + fixture_update_string)
    if float(player_update_string) > float(player_stats_current_version): #compares internal file version with github file version
        print('\nPlayer statistics are out of date')
        player_stats_update_query = input('\nWould you like to update LCFC player statistics? Y / N\n')
        if player_stats_update_query == yes:
            print("Working...")
            os.replace('current_player_stats_version.py', 'current_player_stats_version.old.py') #Goalkeeper version code
            browser.get('https://raw.githubusercontent.com/AliCW/Test/master/current_player_stats_version.py')
            latest_player_stat_version_raw = browser.page_source
            latest_player_stat_version_parsed = html.unescape(latest_player_stat_version_raw)
            latest_player_stat_version_soup = BeautifulSoup(latest_player_stat_version_parsed, features='html.parser')
            latest_player_stat_version_final = latest_player_stat_version_soup.pre.string
            player_version_create = open('current_player_stats_version.py', 'w+')
            player_version_create.write(latest_player_stat_version_final)
            player_version_create.close()
            os.replace('current_player_stats.py', 'current_player_stats.old.py') #Goalkeeper statistic code
            browser.get('https://raw.githubusercontent.com/AliCW/Test/master/current_player_stats.py')
            latest_player_stats_raw = browser.page_source
            latest_player_stat_parsed = html.unescape(latest_player_stats_raw)
            latest_player_stat_soup = BeautifulSoup(latest_player_stat_parsed, features='html.parser')
            latest_player_stat_final = latest_player_stat_soup.pre.string
            player_stats_create = open('current_player_stats.py', 'w+')
            player_stats_create.write(latest_player_stat_final)
            player_stats_create.close()
        if player_stats_update_query == no:
            print("Very well...")
    if float(player_update_string) <= float(player_stats_current_version):
        print('\nPlayer statistic files are up to date!')
    if float(fixture_update_string) > float(fixture_list_current_version):
        print('Fixture list if out of date\n')
        fixture_update_query = input('Would you like to update LCFC fixtures? Y / N\n').lower()
        if fixture_update_query == yes:
            os.replace('current_fixture_version.py', 'current_fixture_version.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/Test/master/current_fixture_version.py')
            latest_fixture_version_raw = browser.page_source
            latest_fixture_version_parsed = html.unescape(latest_fixture_version_raw)
            latest_fixture_version_soup = BeautifulSoup(latest_fixture_version_parsed, features='html.parser')
            latest_fixture_version_final = latest_fixture_version_soup.pre.string
            fixture_version_create = open('current_fixture_version.py', 'w+')
            fixture_version_create.write(latest_fixture_version_final)
            fixture_version_create.close()
            os.replace('current_fixture_list.py', 'current_fixture_list.old.py') #changes current name to .old - delete the .old file maybe within another script / function - MAY NEED AN OVERRIDE FUNCTION FOR THIS
            browser.get('https://raw.githubusercontent.com/AliCW/Test/master/current_fixture_list.py') #goes to the page with latest fixture file raw code
            latest_fixture_code_raw = browser.page_source #copies the raw code
            latest_fixture_code_parsed = html.unescape(latest_fixture_code_raw) #parses the code to retain symbolism
            latest_fixture_code_soup = BeautifulSoup(latest_fixture_code_parsed, features='html.parser')
            latest_fixture_code_final = latest_fixture_code_soup.pre.string
            fixture_page_create = open('current_fixture_list.py', 'w+') #creates the new fixture page
            fixture_page_create.write(latest_fixture_code_final) #writes the code to the new fixture page
            fixture_page_create.close() #closes the new fixture page
            browser.close()
        if fixture_update_query == no:
            print("Very well...")
            browser.close()
    if float(fixture_update_string) <= float(fixture_list_current_version):
        print('\nFixture list files are up to date!')
        browser.close()
    else: player_passed_close_page()
    startupquery00()

def player_passed_close_page():
    print('Update tool has completed')

def startupquery00():
    startquery = input('\nType "stats" for player statistics.\nType "fixtures" for the fixture list.\nType "commands" for a list of other features or "exit" to close the program.\n').lower()
    if (startquery == command): #lists available commands
        list_of_commands()
        startupquery00()
    if (startquery == fixtures):
        subprocess.call(['python', 'current_fixture_list.py'])
        startupquery00()
    if (startquery == statistics):
        subprocess.call(['python', 'current_player_stats.py'])
        startupquery00()
    if (startquery == shut_down):
        sys.exit()

def list_of_commands():
    command_list = input('\nfixtures / stats / update player/or/fixture version\n\nType "reset" to go back to the beginning\n').lower()
    if (command_list == fixtures):
        subprocess.call(['python', 'current_fixture_list.py']) #downloads the new fixture list
        list_of_commands()
    if (command_list == statistics):
        subprocess.call(['python', 'current_player_stats.py'])
        list_of_commands()
    if (command_list == rst1):
        startupquery00()
    if (command_list == fx_version):
        print(float(fixture_list_current_version))
        list_of_commands()
    if (command_list == pl_version):
        print(float(player_stats_current_version))
        list_of_commands()
    else: list_of_commands_failed_syntax()

def list_of_commands_failed_syntax():
    print('\nUnknown command syntax\n')
    list_of_commands()

def fixture_update_loop():
    subprocess.call([])

startuppage()
