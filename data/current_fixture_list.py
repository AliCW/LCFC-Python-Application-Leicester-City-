#v0.15
import sys
import datetime
from itertools import zip_longest
from tabulate import tabulate
current_time = str(datetime.datetime.now())

okay = str('f')
next_fix = str('n')
all = str('all')
latest = str('l')
remain_yes = 0
fix_reverse_list = []

class fixture_date_id: #list of premier league fixtures only!!!
    def leiVsNew(): # starts at the newcastle game because of when the software is written
        if current_time > '2019-09-29 19:00:00.000000': #qualifier to select next match - if the date is higher, it will move to the next
            fixture_date_id.livVsLei() #specifies the next match qualifier to look up - runs in order until date correlates
        else: fixture_info.iLeiVsNew() #specifies the information to print if the qualifier matches - once a match is found, the script then only runs in the fixture_info class
    def livVsLei():
        if current_time > '2019-10-05 17:30:00.000000':
            fixture_date_id.leiVsBur()
        else: fixture_info.iLivVsLei()
    def leiVsBur():
        if current_time > '2019-10-19 17:30:00.000000':
            fixture_date_id.souVsLei()
        else: fixture_info.iLeiVsBur()
    def souVsLei():
        if current_time > '2019-10-25 22:30:00.000000':
            fixture_date_id.butVsLei()
        else: fixture_info.iSouVsLei()
    def butVsLei():
        if current_time > '2019-10-29 22:15:00.000000':
            fixture_date_id.cryVsLei()
        else: fixture_info.iButVsLei()
    def cryVsLei():
        if current_time > '2019-11-03 16:30:00.000000':
            fixture_date_id.leiVsArs()
        else: fixture_info.iCryVsLei()
    def leiVsArs():
        if current_time > '2019-11-09 20:00:00.000000':
            fixture_date_id.bhaVsLei()
        else: fixture_info.iLeiVsArs()
    def bhaVsLei():
        if current_time > '2019-11-23 17:30:00.000000':
            fixture_date_id.leiVsEve()
        else: fixture_info.iBhaVsLei()
    def leiVsEve():
        if current_time > '2019-12-01 19:00:00.000000':
            fixture_date_id.leiVsWat()
        else: fixture_info.iLeiVsEve()
    def leiVsWat():
        if current_time > '2019-12-03 22:15:00.000000':
            fixture_date_id.astVsLei()
        else: fixture_info.iLeiVsWat()
    def astVsLei():
        if current_time > '2019-12-07 17:30:00.000000':
            fixture_date_id.leiVsNor()
        else: fixture_info.iAstVsLei()
    def leiVsNor():
        if current_time > '2019-12-14 17:30:00.000000':
            fixture_date_id.eveVsLei_Carab()
        else: fixture_info.iLeiVsNor()
    def eveVsLei_Carab():
        if current_time > '2019-12-18 22:15:00.000000':
            fixture_date_id.mncVsLei()
        else: fixture_info.iEveVsLei_Carab()
    def mncVsLei():
        if current_time > '2019-12-21 17:30:00.000000':
            fixture_date_id.leiVsLiv()
        else: fixture_info.iMncVsLei()
    def leiVsLiv():
        if current_time > '2019-12-26 22:30:00.000000':
            fixture_date_id.whuVsLei()
        else: fixture_info.iLeiVsLiv()
    def whuVsLei():
        if current_time > '2019-12-28 17:30:00.000000':
            fixture_date_id.newVsLei()
        else: fixture_info.iWhuVsLei()
    def newVsLei():
        if current_time > '2020-01-01 17:30:00.000000':
            fixture_date_id.leiVsWig()
        else: fixture_info.iNewVsLei()
    def leiVsWig():
        if current_time > '2020-01-04 20:31:00.000000':
            fixture_date_id.leiVsAst_Carab()
        else: fixture_info.iLeiVsWig()
    def leiVsAst_Carab():
        if current_time > '2020-01-08 22:30:00.000000':
            fixture_date_id.leiVsSou()
        else: fixture_info.iLeiVsAst_Carab()
    def leiVsSou():
        if current_time > '2020-01-11 17:30:00.000000':
            fixture_date_id.burVsLei()
        else: fixture_info.iLeiVsSou()
    def burVsLei():
        if current_time > '2020-01-19 16:30:00.000000':
            fixture_date_id.leiVsWhu()
        else: fixture_info.iBurVsLei()
    def leiVsWhu():
        if current_time > '2020-01-21 22:00:00.000000':
            fixture_date_id.breVsLei_FA()
        else: fixture_info.iLeiVsWhu()
    def breVsLei_FA():
        if current_time > '2020-01-25 17:30:00.000000':
            fixture_date_id.astVsLei_Carab()
        else: fixture_info.iBreVsLei_FA()
    def astVsLei_Carab():
        if current_time > '2020-01-28 22:15:00.000000':
            fixture_date_id.leiVsChe()
        else: fixture_info.iAstVsLei_Carab()
    def leiVsChe():
        if current_time > '2020-02-01 17:30:00.000000':
            fixture_date_id.wolVsLei()
        else: fixture_info.iLeiVsChe()
    def wolVsLei():
        if current_time > '2020-02-08 17:30:00.000000':
            fixture_date_id.leiVsMnc()
        else: fixture_info.iWolVsLei()
    def leiVsMnc():
        if current_time > '2020-02-22 17:30:00.000000':
            fixture_date_id.norVsLei()
        else: fixture_info.iLeiVsMnc()
    def norVsLei():
        if current_time > '2020-02-29 17:30:00.000000':
            fixture_date_id.leiVsBhc_FA()
        else: fixture_info.iNorVsLei()
    def leiVsBhc_FA():
        if current_time > '2020-03-04 22:15:00.000000':
            fixture_date_id.leiVsAst()
        else: fixture_info.iLeiVsBhc_FA()
    def leiVsAst():
        if current_time > '2020-03-07 17:30:00.000000':
            fixture_date_id.watVsLei()
        else: fixture_info.iLeiVsAst()
    def watVsLei():
        if current_time > '2020-03-14 17:30:00.000000':
            fixture_date_id.leiVsBha()
        else: fixture_info.iWatVsLei()
    def leiVsBha():
        if current_time > '2020-03-21 17:30:00.000000':
            fixture_date_id.eveVsLei()
        else: fixture_info.iLeiVsBha()
    def eveVsLei():
        if current_time > '2020-04-04 17:30:00.000000':
            fixture_date_id.leiVsCry()
        else: fixture_info.iEveVsLei()
    def leiVsCry():
        if current_time > '2020-04-11 17:30:00.000000':
            fixture_date_id.arsVsLei()
        else: fixture_info.iLeiVsCry()
    def arsVsLei():
        if current_time > '2020-04-25 17:30:00.000000':
            fixture_date_id.leiVsShu()
        else: fixture_info.iArsVsLei()
    def leiVsShu():
        if current_time > '2020-05-02 17:30:00.000000':
            fixture_date_id.totVsLei()
        else: fixture_info.iLeiVsShu()
    def totVsLei():
        if current_time > '2020-05-09 17:30:00.000000':
            fixture_date_id.leiVsMnu()
        else: fixture_info.iTotVsLei()
    def leiVsMnu():
        if current_time > '2020-05-17 17:30:00.000000':
            print('No more fixtures to list at this point in time.')
        else: fixture_info.iLeiVsMnu()

class fixture_info: #get international TV schedules from https://www.livesoccertv.com
    def iLeiVsNew(): #test code - def should never be printed - was written after the game was played
        print('Leicester City Vs Newcastle United') #fixture info from LCFC site
        print('Home')
        print('Kick-off: Sunday 29/09/2019 at 16:30')

    def iLivVsLei():
        print('Liverpool FC Vs Leicester City')
        print('Away')
        print('Kick-off: Saturday 05/10/2019 at 15:00')
        next_game_01 = input('\n\nPress N for the next game or any other key to exit\n').lower() #query for the next game?
        if next_game_01 == next_fix:
            fixture_info.iLeiVsBur()
        else: sys.exit()

    def iLeiVsBur():
        print('Leicester City Vs Burnley FC')
        print('Home')
        print('Kick-off: Saturday 19/10/2019 at 15:00')
        next_game_02 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_game_02 == next_fix:
            fixture_info.iSouVsLei()
        else: sys.exit()

    def iSouVsLei():
        print('Southampton FC Vs Leicester City')
        print('Away')
        print('Kick-off: Friday 25/10/2019 at 20:00')
        print('UK Broadcaster: Sky Sports') #Broadcast information from: https://www.premierleague.com/broadcast-schedules
        next_game_03 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_game_03 == next_fix:
            fixture_info.iButVsLei()
        else: sys.exit()

    def iButVsLei():
        print('Burton Albion Vs Leicester City')
        print('Away')
        print('Kick-off: Tuesday 29/10/2019 at 19:45')
        print('UK Broadcaster: None - N/A')
        next_game_cara1 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_game_cara1 == next_fix:
            fixture_info.iCryVsLei()
        else: sys.exit()
        
    def iCryVsLei():
        print('Crystal Palace Vs Leicester City')
        print('Away')
        print('Kick-off: Sunday 03/11/2019 at 14:00')
        print('UK Broadcaster: Sky Sports')
        next_game_04 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_game_04 == next_fix:
            fixture_info.iLeiVsArs()
        else: sys.exit()

    def iLeiVsArs():
        if remain_yes == 0:
            print('\nLeicester City Vs Arsenal FC')
            print('Home')
            print('Kick-off: Saturday 09/11/2019 at 17:30')
            print('UK Broadcaster: Sky Sports')
            next_game_05 = input('\n\nPress N for the next game or any other key to exit\n').lower()
            if next_game_05 == next_fix:
                fixture_info.iBhaVsLei()
            else: sys.exit()
        if remain_yes == 1:
            print('Leicester City Vs Arsenal FC')
            fixture_info.iBhaVsLei()
    def iBhaVsLei():
        if remain_yes == 0:
            print('\nBrighton & Hove Albion Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 23/11/2019 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_06 = input('\n\nPress N for the next game or any other key to exit\n').lower()
            if next_game_06 == next_fix:
                fixture_info.iLeiVsEve()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Brighton & Hove Albion Vs Leicester City']
            #print('Brighton & Hove Albion Vs Leicester City')
            fixture_info.iLeiVsEve()

    def iLeiVsEve():
        if remain_yes == 0:
            print('\nLeicester City Vs Everton FC')
            print('Home')
            print('Kick-off: Sunday 01/12/2019 at 16:30')
            print('UK Broadcaster: Sky Sports')
            next_game_07 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_07 == next_fix:
                fixture_info.iLeiVsWat()
            if next_game_07 == all:
                remain_yes_on()
                fixture_info.iLeiVsWat()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Everton FC']
            #print('Leicester City Vs Everton FC')
            fixture_info.iLeiVsWat()

    def iLeiVsWat():
        if remain_yes == 0:
            print('\nLeicester City Vs Watford FC')
            print('Home')
            print('Kick-off: Tuesday 03/12/2019 at 19:45')
            print('UK Broadcaster: Amazon Prime Video')
            next_game_08 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_08 == next_fix:
                fixture_info.iAstVsLei()
            if next_game_08 == all:
                remain_yes_on()
                fixture_info.iAstVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Watford FC']
            #print('Leicester City Vs Watford FC')
            fixture_info.iAstVsLei()

    def iAstVsLei():
        if remain_yes == 0:
            print('\nAston Villa Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 07/12/2019 at 15:00')
            print('UK Broadcaster: Sky Sports')
            next_game_09 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_09 == next_fix:
                fixture_info.iLeiVsNor()
            if next_game_09 == all:
                remain_yes_on()
                fixture_info.iLeiVsNor()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Aston Villa Vs Leicester City']
            #print('Aston Villa Vs Leicester City')
            fixture_info.iLeiVsNor()

    def iLeiVsNor():
        if remain_yes == 0:
            print('\nLeicester City Vs Norwich City')
            print('Home')
            print('Kick-off: Saturday 14/12/2019 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_10 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_10 == next_fix:
                fixture_info.iEveVsLei_Carab()
            if next_game_10 == all:
                remain_yes_on()
                fixture_info.iEveVsLei_Carab()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Norwich City']
            #print('Leicester City Vs Norwich City')
            fixture_info.iEveVsLei_Carab()
            
    def iEveVsLei_Carab():
        if remain_yes == 0:
            print('\nEverton FC Vs Leicester City (League Cup: Quarter-Final)')
            print('Away')
            print('Kick-off: Wednesday 18/12/2019 at 19:45')
            print('UK Broadcaster: None - N/A')
            print('International Broadcaster(s): ESPN+')
            next_game_001 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_001 == next_fix:
                fixture_info.iMncVsLei()
            if next_game_001 == all:
                remain_yes_on()
                fixture_info.iMncVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Everton FC Vs Leicester City (League Cup: Quarter-Final)']
            #print('Everton FC Vs Leicester City')
            fixture_info.iMncVsLei()
            
    def iMncVsLei():
        if remain_yes == 0:
            print('\nManchester City Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 21/12/2019 at 15:00')
            print('UK Broadcaster: Sky Sports')
            next_game_11 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_11 == next_fix:
                fixture_info.iLeiVsLiv()
            if next_game_11 == all:
                remain_yes_on()
                fixture_info.iLeiVsLiv()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Manchester City Vs Leicester City']
            #print('Manchester City Vs Leicester City')
            fixture_info.iLeiVsLiv()

    def iLeiVsLiv():
        if remain_yes == 0:
            print('\nLeicester City Vs Liverpool FC')
            print('Home')
            print('Kick-off: Thursday 26/12/2019 at 20:00')
            print('UK Broadcaster: Amazon Prime Video')
            next_game_12 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_12 == next_fix:
                fixture_info.iWhuVsLei()
            if next_game_12 == all:
                remain_yes_on()
                fixture_info.iWhuVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Liverpool FC']
            #print('Leicester City Vs Liverpool FC')
            fixture_info.iWhuVsLei()

    def iWhuVsLei():
        if remain_yes == 0:
            print('\nWest Ham United Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 28/12/2019 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_13 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_13 == next_fix:
                fixture_info.iNewVsLei()
            if next_game_13 == all:
                remain_yes_on()
                fixture_info.iNewVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['West Ham United Vs Leicester City']
            #print('West Ham United Vs Leicester City')
            fixture_info.iNewVsLei()

    def iNewVsLei():
        if remain_yes == 0:
            print('\nNewcastle United Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 01/01/2020 at 15:00')
            print('UK Broadcaster: BT Sports')
            next_game_14 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_14 == next_fix:
                fixture_info.iLeiVsWig()
            if next_game_14 == all:
                remain_yes_on()
                fixture_info.iLeiVsWig()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Newcastle United Vs Leicester City']
            #print('Newcastle United Vs Leicester City')
            fixture_info.iLeiVsWig()

    def iLeiVsWig():
        if remain_yes == 0:
            print('\nLeicester City Vs Wigan Athletic (F.A. Cup: 3rd Round)')
            print('Home')
            print('Kick-off: Saturday 04/01/2020 at 17:31')
            print('UK Broadcaster: None - N/A')
            next_game_002 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                  'Press any other key to exit\n').lower()
            if next_game_002 == next_fix:
                fixture_info.iLeiVsAst_Carab()
            if next_game_002 == all:
                remain_yes_on()
                fixture_info.iLeiVsAst_Carab()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Wigan Athletic (F.A. Cup: 3rd Round)']
            fixture_info.iLeiVsAst_Carab()

    def iLeiVsAst_Carab():
        if remain_yes == 0:
            print('\nLeicester City Vs Aston Villa (Carabao Cup: Semi Final 1st leg)')
            print('Home')
            print('Kick-off: Wednesday 08/01/2020 at 20:00')
            print('UK Broadcaster: N/A')
            next_game_003 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                  'Press any other key to exit\n').lower()
            if next_game_003 == next_fix:
                fixture_info.iLeiVsSou()
            if next_game_003 == all:
                remain_yes_on()
                fixture_info.iLeiVsSou()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Aston Villa (Carabao Cup: Semi Final 1st leg)']
            fixture_info.iLeiVsSou()

    def iLeiVsSou():
        if remain_yes == 0:
            print('\nLeicester City Vs Southampton FC')
            print('Home')
            print('Kick-off: Saturday 11/01/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_15 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_15 == next_fix:
                fixture_info.iBurVsLei()
            if next_game_15 == all:
                remain_yes_on()
                fixture_info.iBurVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Southampton FC']
            #print('Leicester City Vs Southampton FC')
            fixture_info.iBurVsLei()

    def iBurVsLei():
        if remain_yes == 0:
            print('\nBurnley FC Vs Leicester City')
            print('Away')
            print('Kick-off: Sunday 19/01/2019 at 14:00')
            print('UK Broadcaster: Sky Sports')
            next_game_16 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_16 == next_fix:
                fixture_info.iLeiVsWhu()
            if next_game_16 == all:
                remain_yes_on()
                fixture_info.iLeiVsWhu()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Burnley FC Vs Leicester City']
            #print('Burnley FC Vs Leicester City')
            fixture_info.iLeiVsWhu()

    def iLeiVsWhu():
        if remain_yes == 0:
            print('\nLeicester City Vs West Ham United')
            print('Home')
            print('Kick-off: Tuesday 21/01/2020 at 19:30')
            print('UK Broadcaster: BT Sports')
            next_game_17 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_17 == next_fix:
                fixture_info.iBreVsLei_FA()
            if next_game_17 == all:
                remain_yes_on()
                fixture_info.iBreVsLei_FA()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs West Ham United']
            #print('Leicester City Vs West Ham United')
            fixture_info.iBreVsLei_FA()

    def iBreVsLei_FA():
        if remain_yes == 0:
            print('\nBrentford FC Vs Leicester City (F.A. Cup 4th Round)')
            print('Away')
            print('Kick-off: Saturday 25/01/2020 at 15:00')
            print('UK Broadcaster: N/A')
            next_game_005 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                  'Press any other key to exit\n').lower()
            if next_game_005 == next_fix:
                fixture_info.iAstVsLei_Carab()
            if next_game_005 == all:
                remain_yes_on()
                fixture_info.iAstVsLei_Carab()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Brentford FC Vs Leicester City (F.A. Cup 4th Round)']
            fixture_info.iAstVsLei_Carab()

    def iAstVsLei_Carab():
        if remain_yes == 0:
            print('\nAston Villa Vs Leicester City (Carabao Cup: Semi final 2nd leg)')
            print('Away')
            print('Kick-off: Tuesday 28/01/2020 at 20:00')
            print('UK Broadcaster: N/A')
            next_game_004 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                  'Press any other key to exit\n').lower()
            if next_game_004 == next_fix:
                fixture_info.iLeiVsChe()
            if next_game_004 == all:
                remain_yes_on()
                fixture_info.iLeiVsChe()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Aston Villa Vs Leicester City (Carabao Cup: Semi final 2nd leg)']
            fixture_info.iLeiVsChe()

    def iLeiVsChe():
        if remain_yes == 0:
            print('\nLeicester City Vs Chelsea FC')
            print('Home')
            print('Kick-off: Saturday 01/02/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_18 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_18 == next_fix:
                fixture_info.iWolVsLei()
            if next_game_18 == all:
                remain_yes_on()
                fixture_info.iWolVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Chelsea FC']
            #print('Leicester City Vs Chelsea FC')
            fixture_info.iWolVsLei()

    def iWolVsLei():
        if remain_yes == 0:
            print('\nWolverhampton Wanderers Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 08/02/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_19 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_19 == next_fix:
                fixture_info.iLeiVsMnc()
            if next_game_19 == all:
                remain_yes_on()
                fixture_info.iLeiVsMnc()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Wolverhampton Wanderers Vs Leicester City']
            #print('Wolverhampton Wanderers Vs Leicester City')
            fixture_info.iLeiVsMnc()

    def iLeiVsMnc():
        if remain_yes == 0:
            print('\nLeicester City Vs Manchester City')
            print('Home')
            print('Kick-off: Saturday 22/02/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_20 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_20 == next_fix:
                fixture_info.iNorVsLei()
            if next_game_20 == all:
                remain_yes_on()
                fixture_info.iNorVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Manchester City']
            #print('Leicester City Vs Manchester City')
            fixture_info.iNorVsLei()

    def iNorVsLei():
        if remain_yes == 0:
            print('\nNorwich City Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 29/02/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_21 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_21 == next_fix:
                fixture_info.iLeiVsBhc_FA()
            if next_game_21 == all:
                remain_yes_on()
                fixture_info.iLeiVsBhc_FA()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Norwich City Vs Leicester City']
            #print('Norwich City Vs Leicester City')
            fixture_info.iLeiVsBhc_FA()

    def iLeiVsBhc_FA():
        if remain_yes == 0:
            print('\nLeicester City Vs Birmingham City (F.A. Cup 4th Round)')
            print('Home')
            print('Kick-off: Wednesday 04/03/2020 at 19:45')
            print('UK Broadcaster: None - N/A')
            next_game_0011032020 = input('\n\nPress N for the next game of ALL to see every fixture\n'
                                         'Press any other key to exit\n').lower()
            if next_game_0011032020 == next_fix:
                fixture_info.iLeiVsAst()
            if next_game_0011032020 == all:
                remain_yes_on()
                fixture_info.iLeiVsAst()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Birmingham City']
            fixture_info.iLeiVsAst()

    def iLeiVsAst():
        if remain_yes == 0:
            print('\nLeicester City Vs Aston Villa')
            print('Home')
            print('Kick-off: Saturday 07/03/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_22 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_22 == next_fix:
                fixture_info.iWatVsLei()
            if next_game_22 == all:
                remain_yes_on()
                fixture_info.iWatVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Aston Villa']
            #print('Leicester City Vs Aston Villa')
            fixture_info.iWatVsLei()

    def iWatVsLei():
        if remain_yes == 0:
            print('\nWatford FC Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 14/03/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_23 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_23 == next_fix:
                fixture_info.iLeiVsBha()
            if next_game_23 == all:
                remain_yes_on()
                fixture_info.iLeiVsBha()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Watford FC Vs Leicester City']
            #print('Watford FC Vs Leicester City')
            fixture_info.iLeiVsBha()

    def iLeiVsBha():
        if remain_yes == 0:
            print('\nLeicester City Vs Brighton & Hove Albion')
            print('Home')
            print('Kick-off: Saturday 21/03/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_24 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_24 == next_fix:
                fixture_info.iEveVsLei()
            if next_game_24 == all:
                remain_yes_on()
                fixture_info.iEveVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Brighton & Hove Albion']
            #print('Leicester City Vs Brighton & Hove Albion')
            fixture_info.iEveVsLei()

    def iEveVsLei():
        if remain_yes == 0:
            print('\nEverton FC Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 04/04/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_25 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_25 == next_fix:
                fixture_info.iLeiVsCry()
            if next_game_25 == all:
                remain_yes_on()
                fixture_info.iLeiVsCry()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Everton FC Vs Leicester City']
            #print('Everton FC Vs Leicester City')
            fixture_info.iLeiVsCry()

    def iLeiVsCry():
        if remain_yes == 0:
            print('\nLeicester City Vs Crystal Palace')
            print('Home')
            print('Kick-off: Saturday 11/04/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_26 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_26 == next_fix:
                fixture_info.iArsVsLei()
            if next_game_26 == all:
                remain_yes_on()
                fixture_info.iArsVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Crystal Palace']
            #print('Leicester City Vs Crystal Palace')
            fixture_info.iArsVsLei()

    def iArsVsLei():
        if remain_yes == 0:
            print('\nArsenal FC Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 18/04/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_27 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_27 == next_fix:
                fixture_info.iBouVsLei()
            if next_game_27 == all:
                remain_yes_on()
                fixture_info.iBouVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Arsenal FC Vs Leicester City']
            #print('Arsenal FC Vs Leicester City')
            fixture_info.iBouVsLei()

    def iBouVsLei():
        if remain_yes == 0:
            print('\nAFC Bournemouth Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 25/04/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_28 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_28 == next_fix:
                fixture_info.iLeiVsShu()
            if next_game_28 == all:
                remain_yes_on()
                fixture_info.iLeiVsShu()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['AFC Bournemouth Vs Leicester City']
            #print('AFC Bournemouth Vs Leicester City')
            fixture_info.iLeiVsShu()

    def iLeiVsShu():
        if remain_yes == 0:
            print('\nLeicester City Vs Sheffield United')
            print('Home')
            print('Kick-off: Saturday 02/05/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_29 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_29 == next_fix:
                fixture_info.iTotVsLei()
            if next_game_29 == all:
                remain_yes_on()
                fixture_info.iTotVsLei()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Sheffield United']
            #print('Leicester City Vs Sheffield United')
            fixture_info.iTotVsLei()

    def iTotVsLei():
        if remain_yes == 0:
            print('\nTottenham Hotspur Vs Leicester City')
            print('Away')
            print('Kick-off: Saturday 09/05/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            next_game_30 = input('\n\nPress N for the next game or ALL to see every fixture\n'
                                 'Press any other key to exit\n').lower()
            if next_game_30 == next_fix:
                fixture_info.iLeiVsMnu()
            if next_game_31 == all:
                remain_yes_on()
                fixture_info.iLeiVsMnu()
            else: sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Tottenham Hotspur Vs Leicester City']
            #print('Tottenham Hotspur Vs Leicester City')
            fixture_info.iLeiVsMnu()

    def iLeiVsMnu():
        if remain_yes == 0:
            print('\nLeicester City Vs Manchester United')
            print('Home')
            print('Kick-off: Saturday 17/05/2020 at 15:00')
            print('UK Broadcaster: None - N/A')
            input('\n\nEnd of fixtures, press any key to exit')
            sys.exit()
        if remain_yes == 1:
            global fix_reverse_list
            fix_reverse_list += ['Leicester City Vs Manchester United']
            fix_reverse_list.reverse()
            print(tabulate(zip_longest(fix_reverse_list)))
            #print('Leicester City Vs Manchester United\n')
            sys.exit()

def fixture_start_query():
    initial_query = input('\nType "all" to see all remaining fixtures, or "l" to see the next game\n').lower()
    if initial_query == latest:
        remain_yes_off()
        fixture_date_id.leiVsNew()
    if initial_query == all:
        remain_yes_on()
        fixture_date_id.leiVsNew()

def remain_yes_off():
    global remain_yes
    remain_yes = 0

def remain_yes_on():
    global remain_yes
    remain_yes = 1

fixture_start_query()
#at the startup, the program creates a string containing the current date -
    #uses this string to match to available fixture dates and show these accourdingly
