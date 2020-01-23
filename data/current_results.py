#v0.20
import sys
import datetime
from itertools import zip_longest
from tabulate import tabulate
current_time = str(datetime.datetime.now())
okay = str('f')
previous_result = str('n')
all = str('all')
prem = str('- Premier League')
carab = str('- Carabao Cup')
fa = str('- F.A. Cup')
remain_result_yes = 0
reverse_list = []

away_vs_ars = str('Arsenal FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_ast = str('Aston Villa 1:4 Leicester City')
away_vs_ast_carab = str('Aston Villa 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_bha = str('Brighton Hove Albion 0:2 Leicester City')
away_vs_bou = str('AFC Bournemouth 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_bre_fa = str('Brentford FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_btn = str('Burton Albion 1:3 Leicester City') #carabao cup
away_vs_bur = str('Burnley FC 2:1 Leicester City')
away_vs_che = str('Chelsea FC 1:1 Leicester City')
away_vs_cry = str('Crystal Palace 0:2 Leicester City')
away_vs_eve = str('Everton FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_eve_carab = str('Everton FC (2pen)2:2(4pen) Leicester City')
away_vs_liv = str('Liverpool FC 2:1 Leicester City')
away_vs_lut_carab = str('Luton Town 0:4 Leicester City') #carabao cup
away_vs_mnc = str('Manchester City 3:1 Leicester City')
away_vs_mnu = str('Manchester United 1:0 Leicester City')
away_vs_new = str('Newcastle United 0:3 Leicester City')
away_vs_new_carab = str('Newcastle United (2pen)1:1(4pen) Leicester City') #carabao cup
away_vs_nor = str('Norwich City 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_sou = str('Southampton FC 0:9 Leicester City')
away_vs_shu = str('Sheffield United 1:2 Leicester City')
away_vs_tot = str('Tottenham Hotspur 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_wat = str('Watford FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_whu = str('West Ham United 1:2 Leicester City')
away_vs_wol = str('Wolverhampton Wanderers 0:0 Leicester City')#<-----------YET TO BE PLAYED
home_vs_ars = str('Leicester City 2:0 Arsenal FC')
home_vs_ast = str('Leicester City 0:0 Aston Villa')#<-----------YET TO BE PLAYED
home_vs_ast_carab = str('Leicester City 1:1 Aston Villa')
home_vs_bha = str('Leicester City 0:0 Brighton Hove Albion')#<-----------YET TO BE PLAYED
home_vs_bou = str('Leicester City 3:1 AFC Bournemouth')
home_vs_bur = str('Leicester City 2:1 Burnley FC')
home_vs_che = str('Leicester City 0:0 Chelsea FC')#<-----------YET TO BE PLAYED
home_vs_cry = str('Leicester City 0:0 Crystal Palace')#<-----------YET TO BE PLAYED
home_vs_eve = str('Leicester City 2:1 Everton FC')
home_vs_liv = str('Leicester City 0:4 Liverpool FC')
home_vs_mnc = str('Leicester City 0:0 Manchester City')#<-----------YET TO BE PLAYED
home_vs_mnu = str('Leicester City 0:0 Manchester United')#<-----------YET TO BE PLAYED
home_vs_new = str('Leicester City 5:0 Newcastle United')
home_vs_nor = str('Leicester City 1:1 Norwich City')#<-----------YET TO BE PLAYED
home_vs_shu = str('Leicester City 0:0 Sheffield United')#<-----------YET TO BE PLAYED
home_vs_sou = str('Leicester City 1:2 Southampton FC')
home_vs_tot = str('Leicester City 2:1 Tottenham Hotspur')
home_vs_wat = str('Leicester City 2:0 Watford FC')
home_vs_whu = str('Leicester City 4:1 West Ham United')
home_vs_wig_fa = str('Leicester City 2:0 Wigan Athletic')
home_vs_wol = str('Leicester City 0:0 Wolverhampton Wanderers')

class latest_result_ident:
    def leiVsBur():
        if current_time > '2019-10-19 17:30:00.000000':
            latest_result_ident.souVsLei()
        else: result_info.fx_LivVsLei()
    def souVsLei():
        if current_time > '2019-10-25 22:30:00.000000':
            latest_result_ident.btnVsLei()
        else: result_info.fx_LeiVsBur()
    def btnVsLei():
        if current_time > '2019-10-29 22:15:00.000000':
            latest_result_ident.cryVsLei()
        else: result_info.fx_SouVsLei()
    def cryVsLei():
        if current_time > '2019-11-03 16:30:00.000000':
            latest_result_ident.leiVsArs()
        else: result_info.fx_BtnVsLei()
    def leiVsArs():
        if current_time > '2019-11-09 20:00:00.000000':
            latest_result_ident.bhaVsLei()
        else: result_info.fx_CryVsLei()
    def bhaVsLei():
        if current_time > '2019-11-23 17:30:00.000000':
            latest_result_ident.leiVsEve()
        else: result_info.fx_LeiVsArs()
    def leiVsEve():
        if current_time > '2019-12-01 19:00:00.000000':
            latest_result_ident.leiVsWat()
        else: result_info.fx_BhaVsLei()
    def leiVsWat():
        if current_time > '2019-12-04 22:15:00.000000':
            latest_result_ident.astVsLei()
        else: result_info.fx_LeiVsEve()
    def astVsLei():
        if current_time > '2019-12-07 17:30:00.000000':
            latest_result_ident.leiVsNor()
        else: result_info.fx_LeiVsWat()
    def leiVsNor():
        if current_time > '2019-12-14 17:30:00.000000':
            latest_result_ident.eveVsLei_Carab()
        else: result_info.fx_AstVsLei()
    def eveVsLei_Carab():
        if current_time > '2019-12-18 22:15:00.000000':
            latest_result_ident.mncVsLei()
        else: result_info.fx_LeiVsNor()
    def mncVsLei():
        if current_time > '2019-12-21 17:30:00.000000':
            latest_result_ident.leiVsLiv()
        else: result_info.fx_EveVsLei_Carab()
    def leiVsLiv():
        if current_time > '2019-12-26 22:30:00.000000':
            latest_result_ident.whuVsLei()
        else: result_info.fx_MncVsLei()
    def whuVsLei():
        if current_time > '2019-12-28 17:30:00.000000':
            latest_result_ident.newVsLei()
        else: result_info.fx_LeiVsLiv()
    def newVsLei():
        if current_time > '2020-01-01 17:30:00.000000':
            latest_result_ident.leiVsWig_fa()
        else: result_info.fx_WhuVsLei()
    def leiVsWig_fa():
        if current_time > '2020-01-04 20:01:00.000000':
            latest_result_ident.leiVsAst_Carab()
        else: result_info.fx_NewVsLei()
    def leiVsAst_Carab():
        if current_time > '2020-01-08 22:30:00.000000':
            latest_result_ident.leiVsSou()
        else: result_info.fx_LeiVsWig_FA()
    def leiVsSou():
        if current_time > '2020-01-11 17:30:00.000000':
            latest_result_ident.burVsLei()
        else: result_info.fx_LeiVsAst_Carab()
    def burVsLei():
        if current_time > '2020-01-18 17:30:00.000000':
            latest_result_ident.leiVsWhu()
        else: result_info.fx_LeiVsSou()
    def leiVsWhu():
        if current_time > '2020-01-21 22:15:00.000000':
            latest_result_ident.breVsLei_FA()
        else: result_info.fx_BurVsLei()
    def breVsLei_FA():
        if current_time > '2020-01-25 17:30:00.000000':
            latest_result_ident.astVsLei_Carab()
        else: result_info.fx_LeiVsWhu()
    def astVsLei_Carab():
        if current_time > '2020-01-28 22:15:00.000000':
            latest_result_ident.leiVsChe()
        else: result_info.fx_BreVsLei_FA()
    def leiVsChe():
        if current_time > '2020-02-01 17:30:00.000000':
            latest_result_ident.wolVsLei()
        else: result_info.fx_AstVsLei_Carab()
    def wolVsLei():
        if current_time > '2020-02-08 17:30:00.000000':
            latest_result_ident.leiVsMnc()
        else: result_info.fx_LeiVsChe()
    def leiVsMnc():
        if current_time > '2020-02-22 17:30:00.000000':
            latest_result_ident.norVsLei()
        else: result_info.fx_WolVsLei()
    def norVsLei():
        if current_time > '2020-02-29 17:30:00.000000':
            latest_result_ident.leiVsAst()
        else: result_info.fx_LeiVsMnc()
    def leiVsAst():
        if current_time > '2020-03-07 17:30:00.000000':
            latest_result_ident.watVsLei()
        else: result_info.fx_NorVsLei()
    def watVsLei():
        if current_time > '2020-03-14 17:30:00.000000':
            latest_result_ident.leiVsBha()
        else: result_info.fx_LeiVsAst()
    def leiVsBha():
        if current_time > '2020-03-21 17:30:00.000000':
            latest_result_ident.eveVsLei()
        else: result_info.fx_WatVsLei()
    def eveVsLei():
        if current_time > '2020-04-04 17:30:00.000000':
            latest_result_ident.leiVsCry()
        else: result_info.fx_LeiVsBha()
    def leiVsCry():
        if current_time > '2020-04-11 17:30:00.000000':
            latest_result_ident.arsVsLei()
        else: result_info.fx_EveVsLei()
    def arsVsLei():
        if current_time > '2020-04-25 17:30:00.000000':
            latest_result_ident.leiVsShu()
        else: result_info.fx_LeiVsCry()
    def leiVsShu():
        if current_time > '2020-05-02 17:30:00.000000':
            latest_result_ident.totVsLei()
        else: result_info.fx_ArsVsLei()
    def totVsLei():
        if current_time > '2020-05-09 17:30:00.000000':
            latest_result_ident.leiVsMnu()
        else: result_info.fx_LeiVsShu()
    def leiVsMnu():
        if current_time > '2020-05-17 17:30:00.000000':
            print('You have reached the end of time.')
        else: result_info.fx_LeiVsMnu()

class result_info:
    def fx_LeiVsWol():
        if remain_result_yes == 0:
            print(home_vs_wol + prem)
            input('\nEnd of results list, press any key to exit')
            sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_wol]
            reverse_list.reverse()
            print(tabulate(zip_longest(reverse_list)))
            sys.exit()
    def fx_CheVsLei():
        if remain_result_yes == 0:
            print(away_vs_che + prem)
            next_res_09 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res_09 == previous_result:
                result_info.fx_LeiVsWol()
            if next_res_09 == all:
                remain_result_yes_on()
                result_info.fx_CheVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_che]
            #print(away_vs_che + prem)
            result_info.fx_LeiVsWol()
    def fx_ShuVsLei():
        if remain_result_yes == 0:
            print(away_vs_shu + prem)
            next_res_08 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res_08 == previous_result:
                result_info.fx_CheVsLei()
            if next_res_08 == all:
                remain_result_yes_on()
                result_info.fx_ShuVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_shu]
            #print(away_vs_shu + prem)
            result_info.fx_CheVsLei()
    def fx_NewVsLei_carab():
        if remain_result_yes == 0:
            print(away_vs_new_carab + carab)
            next_res_07 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res_07 == previous_result:
                result_info.fx_ShuVsLei()
            if next_res_07 == all:
                remain_result_yes_on()
                result_info.fx_NewVsLei_carab()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_new_carab]
            #print(away_vs_new_carab + carab)
            result_info.fx_ShuVsLei()
    def fx_LeiVsBou():
        if remain_result_yes == 0:
            print(home_vs_bou + prem)
            next_res_06 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res_06 == previous_result:
                result_info.fx_NewVsLei_carab()
            if next_res_06 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsBou()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_bou]
            #print(home_vs_bou + prem)
            result_info.fx_NewVsLei_carab()
    def fx_MnuVsLei():
        if remain_result_yes == 0:
            print(away_vs_mnu + prem)
            next_res_05 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res_05 == previous_result:
                result_info.fx_LeiVsBou()
            if next_res_05 == all:
                remain_result_yes_on()
                result_info.fx_MnuVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_mnu]
            #print(away_vs_mnu + prem)
            result_info.fx_LeiVsBou()
    def fx_LeiVsTot():
        if remain_result_yes == 0:
            print(home_vs_tot + prem)
            next_res_04 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res_04 == previous_result:
                result_info.fx_MnuVsLei()
            if next_res_04 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsTot()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_tot]
            #print(home_vs_tot + prem)
            result_info.fx_MnuVsLei()
    def fx_LutVsLei():
        if remain_result_yes == 0:
            print(away_vs_lut_carab + carab)
            next_res03 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res03 == previous_result:
                result_info.fx_LeiVsTot()
            if next_res03 == all:
                remain_result_yes_on()
                result_info.fx_LutVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_lut_carab]
            #print(away_vs_lut_carab + carab)
            result_info.fx_LeiVsTot()
    def fx_LeiVsNew():
        if remain_result_yes == 0:
            print(home_vs_new + prem)
            next_res02 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res02 == previous_result:
                result_info.fx_LutVsLei()
            if next_res02 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsNew()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_new]
            #print(home_vs_new + prem)
            result_info.fx_LutVsLei()
    def fx_LivVsLei():
        if remain_result_yes == 0:
            print(away_vs_liv + prem)
            next_res01 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res01 == previous_result:
                result_info.fx_LeiVsNew()
            if next_res01 == all:
                remain_result_yes_on()
                result_info.fx_LivVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_liv]
            #print(away_vs_liv + prem)
            result_info.fx_LeiVsNew()
    def fx_LeiVsBur():
        if remain_result_yes == 0:
            print(home_vs_bur + prem)
            next_res00 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res00 == previous_result:
                result_info.fx_LivVsLei()
            if next_res00 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsBur()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_bur]
            #print(home_vs_bur + prem)
            result_info.fx_LivVsLei()
    def fx_SouVsLei():
        if remain_result_yes == 0:
            print(away_vs_sou + prem)
            next_res10 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res10 == previous_result:
                result_info.fx_LeiVsBur()
            if next_res10 == all:
                remain_result_yes_on()
                result_info.fx_SouVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_sou]
            #print(away_vs_sou + prem)
            result_info.fx_LeiVsBur()
    def fx_BtnVsLei():
        if remain_result_yes == 0:
            print(away_vs_btn + carab)
            next_res11 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res11 == previous_result:
                result_info.fx_SouVsLei()
            if next_res11 == all:
                remain_result_yes_on()
                result_info.fx_BtnVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_btn]
            #print(away_vs_btn + carab)
            result_info.fx_SouVsLei()
    def fx_CryVsLei():
        if remain_result_yes == 0:
            print(away_vs_cry + prem)
            next_res12 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res12 == previous_result:
                result_info.fx_BtnVsLei()
            if next_res12 == all:
                remain_result_yes_on()
                result_info.fx_CryVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_cry]
            #print(away_vs_cry + prem)
            result_info.fx_BtnVsLei()
    def fx_LeiVsArs():
        if remain_result_yes == 0:
            print(home_vs_ars + prem)
            next_res13 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res13 == previous_result:
                result_info.fx_CryVsLei()
            if next_res13 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsArs()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_ars]
            #print(home_vs_ars + prem)
            result_info.fx_CryVsLei()
    def fx_BhaVsLei():
        if remain_result_yes == 0:
            print(away_vs_bha + prem)
            next_res14 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res14 == previous_result:
                result_info.fx_LeiVsArs()
            if next_res14 == all:
                remain_result_yes_on()
                result_info.fx_BhaVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_bha]
            #print(away_vs_bha + prem)
            result_info.fx_LeiVsArs()
    def fx_LeiVsEve():
        if remain_result_yes == 0:
            print(home_vs_eve + prem)
            next_res15 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res15 == previous_result:
                result_info.fx_BhaVsLei()
            if next_res15 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsEve()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_eve]
            #print(home_vs_eve + prem)
            result_info.fx_BhaVsLei()
    def fx_LeiVsWat():
        if remain_result_yes == 0:
            print(home_vs_wat + prem)
            next_res16 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res16 == previous_result:
                result_info.fx_LeiVsEve()
            if next_res16 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsWat()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_wat]
            #print(home_vs_wat + prem)
            result_info.fx_LeiVsEve()
    def fx_AstVsLei():
        if remain_result_yes == 0:
            print(home_vs_ast + prem)
            next_res17 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res17 == previous_result:
                result_info.fx_LeiVsWat()
            if next_res17 == all:
                remain_result_yes_on()
                result_info.fx_AstVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_ast]
            #print(home_vs_ast + prem)
            result_info.fx_LeiVsWat()
    def fx_LeiVsNor():
        if remain_result_yes == 0:
            print(home_vs_nor + prem)
            next_res18 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res18 == previous_result:
                result_info.fx_AstVsLei()
            if next_res18 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsNor()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_nor]
            #print(home_vs_nor + prem)
            result_info.fx_AstVsLei()
    def fx_EveVsLei_Carab():
        if remain_result_yes == 0:
            print(away_vs_eve_carab + carab)
            next_res001 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res001 == previous_result:
                result_info.fx_LeiVsNor()
            if next_res001 == all:
                remain_result_yes_on()
                result_info.fx_EveVsLei_Carab()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_eve_carab]
            #print(away_vs_eve_carab + carab)
            result_info.fx_LeiVsNor()
    def fx_MncVsLei():
        if remain_result_yes == 0:
            print(away_vs_mnc + prem)
            next_res19 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res19 == previous_result:
                result_info.fx_EveVsLei_Carab()
            if next_res19 == all:
                remain_result_yes_on()
                result_info.fx_MncVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_mnc]
            #print(away_vs_mnc + prem)
            result_info.fx_EveVsLei_Carab()
    def fx_LeiVsLiv():
        if remain_result_yes == 0:
            print(home_vs_liv + prem)
            next_res20 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res20 == previous_result:
                result_info.fx_MncVsLei()
            if next_res20 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsLiv()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_liv]
            #print(home_vs_liv + prem)
            result_info.fx_MncVsLei()
    def fx_WhuVsLei():
        if remain_result_yes == 0:
            print(away_vs_whu + prem)
            next_res21 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res21 == previous_result:
                result_info.fx_LeiVsLiv()
            if next_res21 == all:
                remain_result_yes_on()
                result_info.fx_WhuVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_whu]
            #print(away_vs_whu + prem)
            result_info.fx_LeiVsLiv()
    def fx_NewVsLei():
        if remain_result_yes == 0:
            print(away_vs_new + prem)
            next_res22 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res22 == previous_result:
                result_info.fx_WhuVsLei()
            if next_res22 == all:
                remain_result_yes_on()
                result_info.fx_NewVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_new]
            #print(away_vs_new + prem)
            result_info.fx_WhuVsLei()
    def fx_LeiVsWig_FA():
        if remain_result_yes == 0:
            print(home_vs_wig_fa + fa)
            next_res00241219 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res00241219 == previous_result:
                result_info.fx_NewVsLei()
            if next_res00241219 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsWig_FA()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_wig_fa]
            result_info.fx_NewVsLei()
    def fx_LeiVsAst_Carab():
        if remain_result_yes == 0:
            print(home_vs_ast_carab + carab)
            next_res01241219 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res01241219 == previous_result:
                result_info.fx_LeiVsWig_FA()
            if next_res01241219 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsAst_Carab()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_ast_carab]
            result_info.fx_LeiVsWig_FA()
    def fx_LeiVsSou():
        if remain_result_yes == 0:
            print(home_vs_sou + prem)
            next_res23 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res23 == previous_result:
                result_info.fx_LeiVsAst_Carab()
            if next_res23 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsSou()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_sou]
            #print(home_vs_sou + prem)
            result_info.fx_LeiVsAst_Carab()
    def fx_BurVsLei():
        if remain_result_yes == 0:
            print(away_vs_bur + prem)
            next_res24 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res24 == previous_result:
                result_info.fx_LeiVsSou()
            if next_res24 == all:
                remain_result_yes_on()
                result_info.fx_BurVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_bur]
            #print(away_vs_bur + prem)
            result_info.fx_LeiVsSou()
    def fx_LeiVsWhu():
        if remain_result_yes == 0:
            print(home_vs_whu + prem)
            next_res25 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res25 == previous_result:
                result_info.fx_BurVsLei()
            if next_res25 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsWhu()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_whu]
            #print(home_vs_whu + prem)
            result_info.fx_BurVsLei()
    def fx_BreVsLei_FA():
        if remain_result_yes == 0:
            print(away_vs_bre_fa + fa)
            next_res0007012020 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res0007012020 == previous_result:
                result_info.fx_LeiVsWhu()
            if next_res0007012020 == all:
                remain_result_yes_on()
                result_info.fx_BreVsLei_FA()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_bre_fa]
            result_info.fx_LeiVsWhu()
    def fx_AstVsLei_Carab():
        if remain_result_yes == 0:
            print(away_vs_ast_carab + carab)
            next_res03241219 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res03241219 == previous_result:
                result_info.fx_LeiVsWhu()
            if next_res03241219 == all:
                remain_result_yes_on()
                result_info.fx_AstVsLei_Carab()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_ast_carab]
            result_info.fx_LeiVsWhu()
    def fx_LeiVsChe():
        if remain_result_yes == 0:
            print(home_vs_che + prem)
            next_res26 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res26 == previous_result:
                result_info.fx_AstVsLei_Carab()
            if next_res26 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsChe()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_che]
            #print(home_vs_che + prem)
            result_info.fx_AstVsLei_Carab()
    def fx_WolVsLei():
        if remain_result_yes == 0:
            print(away_vs_wol + prem)
            next_res27 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res27 == previous_result:
                result_info.fx_LeiVsChe()
            if next_res27 == all:
                remain_result_yes_on()
                result_info.fx_WolVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_wol]
            #print(away_vs_wol + prem)
            result_info.fx_LeiVsChe()
    def fx_LeiVsMnc():
        if remain_result_yes == 0:
            print(home_vs_mnc + prem)
            next_res28 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res28 == previous_result:
                result_info.fx_WolVsLei()
            if next_res28 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsMnc()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_mnc]
            #print(home_vs_mnc + prem)
            result_info.fx_WolVsLei()
    def fx_NorVsLei():
        if remain_result_yes == 0:
            print(away_vs_nor + prem)
            next_res29 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res29 == previous_result:
                result_info.fx_LeiVsMnc()
            if next_res29 == all:
                remain_result_yes_on()
                result_info.fx_NorVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_nor]
            #print(away_vs_nor + prem)
            result_info.fx_LeiVsMnc()
    def fx_LeiVsAst():
        if remain_result_yes == 0:
            print(home_vs_ast + prem)
            next_res30 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res30 == previous_result:
                result_info.fx_NorVsLei()
            if next_res30 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsAst()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_ast]
            #print(home_vs_ast + prem)
            result_info.fx_NorVsLei()
    def fx_WatVsLei():
        if remain_result_yes == 0:
            print(away_vs_wat + prem)
            next_res31 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res31 == previous_result:
                result_info.fx_LeiVsAst()
            if next_res31 == all:
                remain_result_yes_on()
                result_info.fx_WatVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_wat]
            #print(away_vs_wat + prem)
            result_info.fx_LeiVsAst()
    def fx_LeiVsBha():
        if remain_result_yes == 0:
            print(home_vs_bha + prem)
            next_res32 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res32 == previous_result:
                result_info.fx_WatVsLei()
            if next_res32 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsBha()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_bha]
            #print(home_vs_bha + prem)
            result_info.fx_WatVsLei()
    def fx_EveVsLei():
        if remain_result_yes == 0:
            print(away_vs_eve + prem)
            next_res33 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res33 == previous_result:
                result_info.fx_LeiVsBha()
            if next_res33 == all:
                remain_result_yes_on()
                result_info.fx_EveVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_eve]
            #print(away_vs_eve + prem)
            result_info.fx_LeiVsBha()
    def fx_LeiVsCry():
        if remain_result_yes == 0:
            print(home_vs_cry + prem)
            next_res34 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res34 == previous_result:
                result_info.fx_EveVsLei()
            if next_res34 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsCry()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_cry]
            #print(home_vs_cry + prem)
            result_info.fx_EveVsLei()
    def fx_ArsVsLei():
        if remain_result_yes == 0:
            print(away_vs_ars + prem)
            next_res35 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res35 == previous_result:
                result_info.fx_LeiVsCry()
            if next_res35 == all:
                remain_result_yes_on()
                result_info.fx_ArsVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [away_vs_ars]
            #print(away_vs_ars + prem)
            result_info.fx_LeiVsCry()
    def fx_LeiVsShu():
        if remain_result_yes == 0:
            print(home_vs_shu + prem)
            next_res36 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res36 == previous_result:
                result_info.fx_ArsVsLei()
            if next_res36 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsShu()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_shu]
            #print(home_vs_shu + prem)
            result_info.fx_ArsVsLei()
    def fx_TotVsLei():
        if remain_result_yes == 0:
            print(away_vs_tot + prem)
            next_res37 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res37 == previous_result:
                result_info.fx_LeiVsShu()
            if next_res37 == all:
                remain_result_yes_on()
                result_info.fx_TotVsLei()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_mnu]
            #print(away_vs_tot + prem)
            result_info.fx_LeiVsShu()
    def fx_LeiVsMnu():
        if remain_result_yes == 0:
            print(home_vs_mnu + prem)
            next_res38 = input('\nPress N for the next game or ALL to see the remaining scores\n'
                               'Press any other key to exit.\n').lower()
            if next_res38 == previous_result:
                result_info.fx_TotVsLei()
            if next_res38 == all:
                remain_result_yes_on()
                result_info.fx_LeiVsMnu()
            else: sys.exit()
        if remain_result_yes == 1:
            global reverse_list
            reverse_list += [home_vs_mnu]
            #print(home_vs_mnu + prem)
            result_info.fx_TotVsLei()

def remain_result_yes_off():
    global remain_result_yes
    remain_result_yes = 0

def remain_result_yes_on():
    global remain_result_yes
    remain_result_yes = 1

def results_start_query():
    initial_query = input('\nType "all" to view all results or "n" to see the latest score\n').lower()
    if initial_query == previous_result:
        remain_result_yes_off()
        latest_result_ident.leiVsBur()
    if initial_query == all:
        remain_result_yes_on()
        latest_result_ident.leiVsArs()

results_start_query()
