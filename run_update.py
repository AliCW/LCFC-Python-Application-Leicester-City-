#v0.04
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

try:#<-----Needs to check the version number in order to update, or decide not to
    open_run_file_version = open(base_path + version_path + 'read_version_run.py')
    open_run_file_version.close()
    run_file_version = subprocess.check_output(['python', base_path + version_path + 'read_version_run.py'])
except IOError:
    print('No read file found for run.py, obtaining one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/version/read_version_run.py')
    WebDriverWait(browser, 10)
    new_run_version_raw = browser.page_source
    new_run_version_parsed = html.unescape(new_run_version_raw)
    new_run_version_soup = BeautifulSoup(new_run_version_parsed, features='html.parser')
    new_run_version_final = new_run_version_soup.pre.string
    run_version_create = open(base_path + version_path + 'read_run_version.py', 'w+')
    run_version_create.write(new_run_version_final)
    run_version_create.close()
    browser.close()
    run_file_version = subprocess.check_output(['python', base_path + version_path + 'read_version_run.py'])

def update_run_file():
    if os.path.exists(base_path + old_path): #checks of the old folder exists - blank folder not hosted on github
        print('Existing .old folder found')
    if not os.path.exists(base_path + old_path): #creates old folder for .old files to be moved
        print('Creating .old folder...')
        os.makedirs(base_path + old_path) #specifies the full directory path
    print('Checking for latest run.py file.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/run.py')
    WebDriverWait(browser, 10)
    run_version_raw = browser.page_source
    run_version_parsed = html.unescape(run_version_raw)
    run_version_soup = BeautifulSoup(run_version_parsed, features='html.parser')
    run_update_string = run_version_soup.pre.string
    run_version_number = run_update_string[2:6]
    print('Latest run.py version: ' + run_version_number)
    if float(run_version_number) > float(run_file_version):
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
            print('run.py has been updated.')
        if run_update_query == no:
            print('Very Well...')
            browser.close()
    if float(run_version_number) <= float(run_file_version):
        browser.close()
        print('run.py is up to date.')
        sys.exit()

update_run_file()
