#v0.03
import subprocess
import html
import os
import sys
from signal import SIGTERM
from os import path
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitCondition
from bs4 import BeautifulSoup as BeautifulSoup

yes = ('y')
no = ('n')
base_path = str(Path(__file__).resolve().parent)
data_path = str('\\data\\')
version_path = str('\\version\\')
old_path = str('\\old\\')
double_dash = str('\\')

def check_gecko():
    obtain_gecko_path = subprocess.check_output(['python', 'get_gecko_path.py']).strip() #outputs into bytes
    string_gecko_path = obtain_gecko_path.decode('utf-8') #decode bytes into string
    obtain_gecko_pid = subprocess.check_output(['python', 'get_gecko_pid.py']) #outputs into bytes
    string_gecko_pid = obtain_gecko_pid.decode('utf-8') #decode bytes into string
    int_gecko_pid = int(string_gecko_pid) #convert string to integer - couldnt figure out a way to decode into an integer yet!
    if not int_gecko_pid: #if this string is empty, print statement &  move on
        print('No PID found for geckodriver')
    if not string_gecko_path:  #if this string is empty, print statement &  move on
        print('No path found for geckodriver') #because of the placement of this definition, these statements should never arise
    if string_gecko_path == base_path:
        os.kill(int_gecko_pid, SIGTERM)
        print('Update process is over.')
    else: print('Error in check_gecko, geckodriver.exe may still be running.')

try:#<-----Needs to check the version number in order to update, or decide not to
    open_run_file_version = open(base_path + version_path + 'read_version_run.py')
    open_run_file_version.close()
    run_file_version = subprocess.check_output(['python', base_path + version_path + 'read_version_run.py'])
except IOError:
    print('No version file found for run.py, obtaining one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/run_version.py')
    WebDriverWait(browser, 10)
    new_run_version_raw = browser.page_source
    new_run_version_parsed = html.unescape(new_run_version_raw)
    new_run_version_soup = BeautifulSoup(new_run_version_parsed, features='html.parser')
    new_run_version_final = new_run_version_soup.pre.string
    run_version_create = open(base_path + version_path + 'read_run_version.py', 'w+')
    run_version_create.write(new_run_version_final)
    run_version_create.close()
    browser.close()
    check_gecko()
    run_file_version = subprocess.check_output(['python', base_path + version_path + 'read_version_run.py'])

def update_run_file():
    print('Checking for latest run.py file.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/update/update_table.txt')
    WebDriverWait(browser, 10)
    update_list = browser.page_source
    escape_list = html.unescape(update_list)
    run_soup = BeautifulSoup(escape_list, features='html.parser')
    run_update_string = run_soup.h2.string
    print('Latest run.py version: ' + run_update_string)
    if float(run_update_string) > float(run_file_version):
        run_update_query = input('\nThe run.py file is out of date.\nWould you like to update? Y / N\n').lower()
        if run_update_query == yes:
            os.replace(base_path + double_dash + 'run.py', base_path + old_path + 'run.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/run.py')
            WebDriverWait(browser, 10)
            latest_run_raw = browser.page_source
            latest_run_parsed = html.unescape(latest_run_raw)
            latest_run_soup = BeautifulSoup(latest_run_parsed, features='html.parser')
            latest_run_final = latest_run_soup.pre.string
            run_create = open(base_path + double_dash + 'run.py', 'w+')
            run_create.write(latest_run_final)
            run_create.close()
            browser.close()
            check_gecko()
            print('run.py has been updated.')
        if run_update_query == no:
            print('Very Well...')
            browser.close()
            check_gecko()
    if float(run_update_string) <= float(run_file_version):
        browser.close()
        check_gecko()
        print('run.py is up to date.')
        sys.exit()

update_run_file()
