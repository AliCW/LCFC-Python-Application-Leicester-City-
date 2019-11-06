#revision 0.06
import sys
import datetime
current_time = str(datetime.datetime.now())

okay = str("f")
next_fix = str("n")

class fixture_date_id: #list of premier league fixtures only!!!
    def leiVsNew(): # starts at the newcastle game because of when the software is written
        if current_time > "2019-09-29 19:00:00.000000": #qualifier to select next match - if the date is higher, it will move to the next
            fixture_date_id.livVsLei() #specifies the next match qualifier to look up - runs in order until date correlates
        else: fixture_info.iLeiVsNew() #specifies the information to print if the qualifier matches - once a match is found, the script then only runs in the fixture_info class
    def livVsLei():
        if current_time > "2019-10-05 17:30:00.000000":
            fixture_date_id.leiVsBur()
        else: fixture_info.iLivVsLei()
    def leiVsBur():
        if current_time > "2019-10-19 17:30:00.000000":
            fixture_date_id.souVsLei()
        else: fixture_info.iLeiVsBur()
    def souVsLei():
        if current_time > "2019-10-25 22:30:00.000000":
            fixture_date_id.butVsLei()
        else: fixture_info.iSouVsLei()
    def butVsLei():
        if current_time > "2019-10-29 22:15:00.000000":
            fixture_date_id.cryVsLei()
        else: fixture_info.iButVsLei()
    def cryVsLei():
        if current_time > "2019-11-03 16:30:00.000000":
            fixture_date_id.leiVsArs()
        else: fixture_info.iCryVsLei()
    def leiVsArs():
        if current_time > "2019-11-09 20:00:00.000000":
            fixture_date_id.bhaVsLei()
        else: fixture_info.iLeiVsArs()
    def bhaVsLei():
        if current_time > "2019-11-23 17:30:00.000000":
            fixture_date_id.leiVsEve()
        else: fixture_info.iBhaVsLei()
    def leiVsEve():
        if current_time > "2019-12-01 19:00:00.000000":
            fixture_date_id.leiVsWat()
        else: fixture_info.iLeiVsEve()
    def leiVsWat():
        if current_time > "2019-12-03 22:15:00.000000":
            fixture_date_id.astVsLei()
        else: fixture_info.iLeiVsWat()
    def astVsLei():
        if current_time > "2019-12-07 17:30:00.000000":
            fixture_date_id.leiVsNor()
        else: fixture_info.iAstVsLei()
    def leiVsNor():
        if current_time > "2019-12-14 17:30:00.000000":
            fixture_date_id.eveVsLei_Carab()
        else: fixture_info.iLeiVsNor()
    def eveVsLei_Carab():
        if current_time > "2019-12-18 22:15:00.000000":
            fixture_date_id.mncVsLei()
        else: fixture_info.iEveVsLei_Carab()
    def mncVsLei():
        if current_time > "2019-12-21 17:30:00.000000":
            fixture_date_id.leiVsLiv()
        else: fixture_info.iMncVsLei()
    def leiVsLiv():
        if current_time > "2019-12-26 22:30:00.000000":
            fixture_date_id.whuVsLei()
        else: fixture_info.iLeiVsLiv()
    def whuVsLei():
        if current_time > "2019-12-28 17:30:00.000000":
            fixture_date_id.newVsLei()
        else: fixture_info.iWhuVsLei()
    def newVsLei():
        if current_time > "2020-01-01 17:30:00.000000":
            fixture_date_id.leiVsSou()
        else: fixture_info.iNewVsLei()
    def leiVsSou():
        if current_time > "2020-01-11 17:30:00.000000":
            fixture_date_id.burVsLei()
        else: fixture_info.iLeiVsSou()
    def burVsLei():
        if current_time > "2020-01-18 17:30:00.000000":
            fixture_date_id.leiVsWhu()
        else: fixture_info.iBurVsLei()
    def leiVsWhu():
        if current_time > "2020-01-21 22:15:00.000000":
            fixture_date_id.leiVsChe()
        else: fixture_info.iLeiVsWhu()
    def leiVsChe():
        if current_time > "2020-02-01 17:30:00.000000":
            fixture_date_id.wolVsLei()
        else: fixture_info.iLeiVsChe()
    def wolVsLei():
        if current_time > "2020-02-08 17:30:00.000000":
            fixture_date_id.leiVsMnc()
        else: fixture_info.iWolVsLei()
    def leiVsMnc():
        if current_time > "2020-02-22 17:30:00.000000":
            fixture_date_id.norVsLei()
        else: fixture_info.iLeiVsMnc()
    def norVsLei():
        if current_time > "2020-02-29 17:30:00.000000":
            fixture_date_id.leiVsAst()
        else: fixture_info.iNorVsLei()
    def leiVsAst():
        if current_time > "2020-03-07 17:30:00.000000":
            fixture_date_id.watVsLei()
        else: fixture_info.iLeiVsAst()
    def watVsLei():
        if current_time > "2020-03-14 17:30:00.000000":
            fixture_date_id.leiVsBha()
        else: fixture_info.iWatVsLei()
    def leiVsBha():
        if current_time > "2020-03-21 17:30:00.000000":
            fixture_date_id.eveVsLei()
        else: fixture_info.iLeiVsBha()
    def eveVsLei():
        if current_time > "2020-04-04 17:30:00.000000":
            fixture_date_id.leiVsCry()
        else: fixture_info.iEveVsLei()
    def leiVsCry():
        if current_time > "2020-04-11 17:30:00.000000":
            fixture_date_id.arsVsLei()
        else: fixture_info.iLeiVsCry()
    def arsVsLei():
        if current_time > "2020-04-25 17:30:00.000000":
            fixture_date_id.leiVsShu()
        else: fixture_info.iArsVsLei()
    def leiVsShu():
        if current_time > "2020-05-02 17:30:00.000000":
            fixture_date_id.totVsLei()
        else: fixture_info.iLeiVsShu()
    def totVsLei():
        if current_time > "2020-05-09 17:30:00.000000":
            fixture_date_id.leiVsMnu()
        else: fixture_info.iTotVsLei()
    def leiVsMnu():
        if current_time > "2020-05-17 17:30:00.000000":
            print("No more fixtures to list at this point in time.")
        else: fixture_info.iLeiVsMnu()

class fixture_info: #get international TV schedules from https://www.livesoccertv.com
    def iLeiVsNew(): #test code - def should never be printed - was written after the game was played
        print("Leicester City Vs Newcastle United") #fixture info from LCFC site
        print("Home")
        print("Kick-off: Sunday 29/09/2019 at 16:30")

    def iLivVsLei():
        print("Liverpool FC Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 05/10/2019 at 15:00")
        next_game_01 = input("\n\nPress N for the next game or any other key to exit\n").lower() #query for the next game?
        if next_game_01 == next_fix:
            fixture_info.iLeiVsBur()
        else: sys.exit()

    def iLeiVsBur():
        print("Leicester City Vs Burnley FC")
        print("Home")
        print("Kick-off: Saturday 19/10/2019 at 15:00")
        next_game_02 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_02 == next_fix:
            fixture_info.iSouVsLei()
        else: sys.exit()

    def iSouVsLei():
        print("Southampton FC Vs Leicester City")
        print("Away")
        print("Kick-off: Friday 25/10/2019 at 20:00")
        print("UK Broadcaster: Sky Sports") #Broadcast information from: https://www.premierleague.com/broadcast-schedules
        next_game_03 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_03 == next_fix:
            fixture_info.iButVsLei()
        else: sys.exit()

    def iButVsLei():
        print("Burton Albion Vs Leicester City")
        print("Away")
        print("Kick-off: Tuesday 29/10/2019 at 19:45")
        print("UK Broadcaster: None - N/A")
        next_game_cara1 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_cara1 == next_fix:
            fixture_info.iCryVsLei()
        else: sys.exit()
        
    def iCryVsLei():
        print("Crystal Palace Vs Leicester City")
        print("Away")
        print("Kick-off: Sunday 03/11/2019 at 14:00")
        print("UK Broadcaster: Sky Sports")
        next_game_04 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_04 == next_fix:
            fixture_info.iLeiVsArs()
        else: sys.exit()

    def iLeiVsArs():
        print("Leicester City Vs Arsenal FC")
        print("Home")
        print("Kick-off: Saturday 09/11/2019 at 17:30")
        print("UK Broadcaster: Sky Sports")
        next_game_05 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_05 == next_fix:
            fixture_info.iBhaVsLei()
        else: sys.exit()

    def iBhaVsLei():
        print("Brighton & Hove Albion Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 23/11/2019 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_06 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_06 == next_fix:
            fixture_info.iLeiVsEve()
        else: sys.exit()

    def iLeiVsEve():
        print("Leicester City Vs Everton FC")
        print("Home")
        print("Kick-off: Sunday 01/12/2019 at 16:30")
        print("UK Broadcaster: Sky Sports")
        next_game_07 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_07 == next_fix:
            fixture_info.iLeiVsWat()
        else: sys.exit()

    def iLeiVsWat():
        print("Leicester City Vs Watford FC")
        print("Home")
        print("Kick-off: Tuesday 03/12/2019 at 19:45")
        print("UK Broadcaster: Amazon Prime Video")
        next_game_08 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_08 == next_fix:
            fixture_info.iAstVsLei()
        else: sys.exit()

    def iAstVsLei():
        print("Aston Villa Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 07/12/2019 at 15:00")
        print("UK Broadcaster: Sky Sports")
        next_game_09 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_09 == next_fix:
            fixture_info.iLeiVsNor()
        else: sys.exit()

    def iLeiVsNor():
        print("Leicester City Vs Norwich City")
        print("Home")
        print("Kick-off: Saturday 14/12/2019 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_10 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_10 == next_fix:
            fixture_info.iEveVsLei_Carab()
        else: sys.exit()
            
    def iEveVsLei_Carab():
        print("Everton FC Vs Leicester City")
        print("Away")
        print("Kick-off: Wednesday 18/12/2019 at 19:45")
        print("UK Broadcaster: None - N/A")
        print("International Broadcaster(s): ESPN+")
        next_game_001 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_001 == next_fix:
            fixture_info.iMncVsLei()
        else: sys.exit() 
            
    def iMncVsLei():
        print("Manchester City Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 21/12/2019 at 15:00")
        print("UK Broadcaster: Sky Sports")
        next_game_11 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_11 == next_fix:
            fixture_info.iLeiVsLiv()
        else: sys.exit()

    def iLeiVsLiv():
        print("Leicester City Vs Liverpool FC")
        print("Home")
        print("Kick-off: Thursday 26/12/2019 at 20:00")
        print("UK Broadcaster: Amazon Prime Video")
        next_game_12 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_12 == next_fix:
            fixture_info.iWhuVsLei()
        else: sys.exit()

    def iWhuVsLei():
        print("West Ham United Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 28/12/2019 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_13 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_13 == next_fix:
            fixture_info.iNewVsLei()
        else: sys.exit()

    def iNewVsLei():
        print("Newcastle United Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 01/01/2020 at 15:00")
        print("UK Broadcaster: BT Sports")
        next_game_14 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_14 == next_fix:
            fixture_info.iLeiVsSou()
        else: sys.exit()

    def iLeiVsSou():
        print("Leicester City Vs Southampton FC")
        print("Home")
        print("Kick-off: Saturday 11/01/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_15 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_15 == next_fix:
            fixture_info.iBurVsLei()
        else: sys.exit()

    def iBurVsLei():
        print("Burnley FC Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 18/01/2019 at 15:00")
        print("UK Broadcaster: Sky Sports")
        next_game_16 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_16 == next_fix:
            fixture_info.iLeiVsWhu()
        else: sys.exit()

    def iLeiVsWhu():
        print("Leicester City Vs West Ham United")
        print("Home")
        print("Kick-off: Tuesday 21/01/2020 at 19:45")
        print("UK Broadcaster: BT Sports")
        next_game_17 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_17 == next_fix:
            fixture_info.iLeiVsChe()
        else: sys.exit()

    def iLeiVsChe():
        print("Leicester City Vs Chelsea FC")
        print("Home")
        print("Kick-off: Saturday 01/02/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_18 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_18 == next_fix:
            fixture_info.iWolVsLei()
        else: sys.exit()

    def iWolVsLei():
        print("Wolverhampton Wanderers Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 08/02/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_19 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_19 == next_fix:
            fixture_info.iLeiVsMnc()
        else: sys.exit()

    def iLeiVsMnc():
        print("Leicester City Vs Manchester City")
        print("Home")
        print("Kick-off: Saturday 22/02/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_20 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_20 == next_fix:
            fixture_info.iNorVsLei()
        else: sys.exit()

    def iNorVsLei():
        print("Norwich City Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 29/02/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_21 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_21 == next_fix:
            fixture_info.iLeiVsAst()
        else: sys.exit()

    def iLeiVsAst():
        print("Leicester City Vs Aston Villa")
        print("Home")
        print("Kick-off: Saturday 07/03/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_22 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_22 == next_fix:
            fixture_info.iWatVsLei()
        else: sys.exit()

    def iWatVsLei():
        print("Watford FC Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 14/03/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_23 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_23 == next_fix:
            fixture_info.iLeiVsBha()
        else: sys.exit()

    def iLeiVsBha():
        print("Leicester City Vs Brighton & Hove Albion")
        print("Home")
        print("Kick-off: Saturday 21/03/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_24 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_24 == next_fix:
            fixture_info.iEveVsLei()
        else: sys.exit()

    def iEveVsLei():
        print("Everton FC Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 04/04/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_25 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_25 == next_fix:
            fixture_info.iLeiVsCry()
        else: sys.exit()

    def iLeiVsCry():
        print("Leicester City Vs Crystal Palace")
        print("Home")
        print("Kick-off: Saturday 11/04/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_26 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_26 == next_fix:
            fixture_info.iArsVsLei()
        else: sys.exit()

    def iArsVsLei():
        print("Arsenal FC Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 18/04/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_27 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_27 == next_fix:
            fixture_info.iBouVsLei()
        else: sys.exit()

    def iBouVsLei():
        print("AFC Bournemouth Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 25/04/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_28 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_28 == next_fix:
            fixture_info.iLeiVsShu()
        else: sys.exit()

    def iLeiVsShu():
        print("Leicester City Vs Sheffield United")
        print("Home")
        print("Kick-off: Saturday 02/05/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_29 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_29 == next_fix:
            fixture_info.iTotVsLei()
        else: sys.exit()

    def iTotVsLei():
        print("Tottenham Hotspur Vs Leicester City")
        print("Away")
        print("Kick-off: Saturday 09/05/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        next_game_30 = input("\n\nPress N for the next game or any other key to exit\n").lower()
        if next_game_30 == next_fix:
            fixture_info.iLeiVsMnu()
        else: sys.exit()

    def iLeiVsMnu():
        print("Leicester City Vs Manchester United")
        print("Home")
        print("Kick-off: Saturday 17/05/2020 at 15:00")
        print("UK Broadcaster: None - N/A")
        input("\n\nEnd of fixtures, press any key to exit")
        sys.exit()

fixture_date_id.leiVsNew()

#at the startup, the program creates a string containing the current date -
    #uses this string to match to available fixture dates and show these accourdingly
