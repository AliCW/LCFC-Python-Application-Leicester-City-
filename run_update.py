import subprocess
import html
import os
import sys
import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitCondition
from bs4 import BeautifulSoup as BeautifulSoup

yes = ('y')
no = ('n')

try:#<-----Needs to check the version number in order to update, or decide not to
    open_run_file_version = open('run_version.py')
    open_run_file_version.close()
    run_file_version = subprocess.check_output(['python', 'run_version.py'])
except IOError:
    print('No version file found for run.py, obtaining one.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/run_version.py')
    WebDriverWait(browser, 10)
    new_run_version_raw = browser.page_source
    new_run_version_parsed = html.unescape(new_run_version_raw)
    new_run_version_soup = BeautifulSoup(new_run_version_parsed, features='html.parser')
    new_run_version_final = new_run_version_soup.pre.string
    run_version_create = open('run_version.py', 'w+')
    run_version_create.write(new_run_version_final)
    run_version_create.close()
    browser.close()
    run_file_version = subprocess.check_output(['python', 'run_version.py'])

def update_run_file():
    print('Checking for latest run.py file.')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/update_table.txt')
    WebDriverWait(browser, 10)
    update_list = browser.page_source
    escape_list = html.unescape(update_list)
    run_soup = BeautifulSoup(escape_list, features='html.parser')
    run_update_string = run_soup.h2.string
    print('Latest run.py version: ' + run_update_string)
    if float(run_update_string) > float(run_file_version):
        run_update_query = input('\nThe run.py file is out of date.\nWould you like to update? Y / N\n').lower()
        if run_update_query == yes:
            os.replace('run_version.py', 'run_version.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/run_version.py')
            WebDriverWait(browser, 10)
            latest_run_version_raw = browser.page_source
            latest_run_version_parsed = html.unescape(latest_run_version_raw)
            latest_run_version_soup = BeautifulSoup(latest_run_version_parsed, features='html.parser')
            latest_run_version_final = latest_run_version_soup.pre.string
            run_version_create_0 = open('run_version.py', 'w+')
            run_version_create_0.write(latest_run_version_final)
            run_version_create_0.close()
            os.replace('run.py', 'run.old.py')
            browser.get('https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/run.py')
            WebDriverWait(browser, 10)
            latest_run_raw = browser.page_source
            latest_run_parsed = html.unescape(latest_run_raw)
            latest_run_soup = BeautifulSoup(latest_run_parsed, features='html.parser')
            latest_run_final = latest_run_soup.pre.string
            run_create = open('run.py', 'w+')
            run_create.write(latest_run_final)
            run_create.close()
            browser.close()
            print('run.py has been updated.')
        if run_update_query == no:
            print('Very Well...')
            browser.close()
    if float(run_update_string) <= float(run_file_version):
        print('run.py is up to date.')
        browser.close()
        sys.exit()

update_run_file()
