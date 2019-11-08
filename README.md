# LCFC python application for Windows (Leicester City Football Club)
Attempting to write a basic program that will quickly tell users statistics, fixtures, scores & other information on Leicester City without having to manually search the internet. This is the second program i've ever created so there may be various inefficencies and i am always welcome to advice if anyone ever finds this or wants to contribute.

I am also working on a Linux version, soon to come.

Below is a brief outline of what each script attempts to accomplish:

# run.py
The main script used to start the application. This script acts as a central point for initial user queries concerning what data they would like to view. The file performs initial checks on its current file version numbers.

It then compares this reference to the version listed online on the update_table.txt (current link: https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/update_table.txt )(IS1) and those within the programs internal version files, e.g. current_fixture_version.py

If the version number from update_table.txt is higher, the program will query the user to update or continue using old files. 

  The update mechanism renames it's current related scripts (.old) then uses headless firefox & geckodriver to go to the embedded update link, copy the page source & parsing with BeautifulSoup then copying this into a new file. The process also performs the same function with version file scripts.

User is presented with the main query listing functions & required input. Data is held on external script files (current_fixture_list.py, current_player_stats.py, current_results.py)

There is also a command function added to help with testing the program.

# update_table.txt
A useless file from the user's end, only used as a reference for the update mechanism (current link: https://raw.githubusercontent.com/AliCW/LCFC-Python-Application-Leicester-City-/master/update_table.txt ) (IS2).

# current_xyz_version.py
All version files have an almost identical syntax with all outputting the current version number of its associated file. These are implemented for the update mechanism to capture their output and compare to the version number hosted online at update_table.txt (IMP1).

# current_fixture_list.py
User is presented with a query asking to see the next fixture, or a list of all. More details are available if viewed one by one. If all associated data is all listed together, it becomes unreadable, therefore, the list of all fixtures only contains limited related information.

No matter which query is selected, the next fixture to be played is always listed first and so on from there. It performs this by taking a timestamp value based on the current time and compares this to timings related to fixtures and outputs data accourdingly (IMP2).

# current_results.py
Works in a similar way to current_fixture_list.py using timestamps to identify the latest result and print accourdingly.

# current_player_stats.py
File is currently just a shell containing no correct data (IMP3). Statistics can be viewed via typing the name or initials of the desired player at the initial user query. There is also a list squad option to view possible entries.

# Improve <-------------------------
IMP1: Possibly find a way of embedding this process into the date files themselves, would make the update process much more simple.

IMP2: Add additional data that might be useful - e.g. international broadcast information.

IMP3: Need to add the data and work on refining applicable information for this file!

# Issues <---------------------------
Would be ideal to add a basic UI at some point - android, win, linux etc. Program lacks 'real-world' application and this would definitaly help.

IS1: Problem with links and testing them - because they are hosted on the 'master' branch, you come into issues when testing.
Might be useful to find an alternative method of hosting or testing new methods & scripts.
  
IS2: Should maybe find a method in which the user doesnt download the update_table.txt file as it has no purpose when downloaded. Maybe find an alternative place to host the file? Possibly a way to make these dynamic?
