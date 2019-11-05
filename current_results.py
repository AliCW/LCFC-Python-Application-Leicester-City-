#revision 0.02
import sys
import datetime
current_time = str(datetime.datetime.now())
print(current_time)
okay = str("f")
previous_result = str("n")
prem = str('- Premier League')
carab = str('- Carabao Cup')
fa = str('- F.A. Cup')

away_vs_ars = str('Arsenal FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_ast = str('Aston Villa 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_bha = str('Brighton Hove Albion 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_bou = str('AFC Bournemouth 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_btn = str('Burton Albion 1:3 Leicester City') #carabao cup
away_vs_bur = str('Burnley FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_che = str('Chelsea FC 1:1 Leicester City')
away_vs_cry = str('Crystal Palace 0:2 Leicester City')#<-----------YET TO BE PLAYED
away_vs_eve = str('Everton FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_liv = str('Liverpool FC 2:1 Leicester City')
away_vs_lut_carab = str('Luton Town 0:4 Leicester City') #carabao cup
away_vs_mnc = str('Manchester City 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_mnu = str('Manchester United 1:0 Leicester City')
away_vs_new = str('Newcastle United 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_new_carab = str('Newcastle United (2pen)1:1(4pen) Leicester City') #carabao cup
away_vs_nor = str('Norwich City 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_sou = str('Southampton FC 0:9 Leicester City')
away_vs_shu = str('Sheffield United 1:2 Leicester City')
away_vs_tot = str('Tottenham Hotspur 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_wat = str('Watford FC 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_whu = str('West Ham United 0:0 Leicester City')#<-----------YET TO BE PLAYED
away_vs_wol = str('Wolverhampton Wanderers 0:0 Leicester City')#<-----------YET TO BE PLAYED
home_vs_ars = str('Leicester City 0:0 Arsenal FC') #<-----------YET TO BE PLAYED
home_vs_ast = str('Leicester City 0:0 Aston Villa')#<-----------YET TO BE PLAYED
home_vs_bha = str('Leicester City 0:0 Brighton Hove Albion')#<-----------YET TO BE PLAYED
home_vs_bou = str('Leicester City 3:1 AFC Bournemouth')
home_vs_bur = str('Leicester City 2:1 Burnley FC')
home_vs_che = str('Leicester City 0:0 Chelsea FC')#<-----------YET TO BE PLAYED
home_vs_cry = str('Leicester City 0:0 Crystal Palace')#<-----------YET TO BE PLAYED
home_vs_eve = str('Leicester City 0:0 Everton FC')#<-----------YET TO BE PLAYED
home_vs_liv = str('Leicester City 0:0 Liverpool FC')#<-----------YET TO BE PLAYED
home_vs_mnc = str('Leicester City 0:0 Manchester City')#<-----------YET TO BE PLAYED
home_vs_mnu = str('Leicester City 0:0 Manchester United')#<-----------YET TO BE PLAYED
home_vs_new = str('Leicester City 5:0 Newcastle United')
home_vs_nor = str('Leicester City 0:0 Norwich City')#<-----------YET TO BE PLAYED
home_vs_shu = str('Leicester City 0:0 Sheffield United')#<-----------YET TO BE PLAYED
home_vs_sou = str('Leicester City 0:0 Southampton FC')#<-----------YET TO BE PLAYED
home_vs_tot = str('Leicester City 2:1 Tottenham Hotspur')
home_vs_wat = str('Leicester City 0:0 Watford FC')#<-----------YET TO BE PLAYED
home_vs_whu = str('Leicester City 0:0 West Ham United')#<-----------YET TO BE PLAYED
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
        if current_time > '2019-12-03 22:15:00.000000':
            latest_result_ident.astVsLei()
        else: result_info.fx_LeiVsEve()
    def astVsLei():
        if current_time > '2019-12-07 17:30:00.000000':
            latest_result_ident.leiVsNor()
        else: result_info.fx_LeiVsWat()
    def leiVsNor():
        if current_time > '2019-12-14 17:30:00.000000':
            latest_result_ident.mncVsLei()
        else: result_info.fx_AstVsLei()
    def mncVsLei():
        if current_time > '2019-12-21 17:30:00.000000':
            latest_result_ident.leiVsLiv()
        else: result_info.fx_LeiVsNor()
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
            latest_result_ident.leiVsSou()
        else: result_info.fx_WhuVsLei()
    def leiVsSou():
        if current_time > '2020-01-11 17:30:00.000000':
            latest_result_ident.burVsLei()
        else: result_info.fx_NewVsLei()
    def burVsLei():
        if current_time > '2020-01-18 17:30:00.000000':
            latest_result_ident.leiVsWhu()
        else: result_info.fx_LeiVsSou()
    def leiVsWhu():
        if current_time > '2020-01-21 22:15:00.000000':
            latest_result_ident.leiVsChe()
        else: result_info.fx_BurVsLei()
    def leiVsChe():
        if current_time > '2020-02-01 17:30:00.000000':
            latest_result_ident.wolVsLei()
        else: result_info.fx_LeiVsWhu()
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
        print(home_vs_wol + prem)
        input('\n\nEnd of results list, press any key to exit')
        sys.exit()
    def fx_CheVsLei():
        print(away_vs_che + prem)
        next_res_09 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res_09 == previous_result:
            result_info.fx_LeiVsWol()
        else: sys.exit()
    def fx_ShuVsLei():
        print(away_vs_shu + prem)
        next_res_08 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res_08 == previous_result:
            result_info.fx_CheVsLei()
        else: sys.exit()
    def fx_NewVsLei_carab():
        print(away_vs_new_carab + carab)
        next_res_07 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res_07 == previous_result:
            result_info.fx_ShuVsLei()
        else: sys.exit()
    def fx_LeiVsBou():
        print(home_vs_bou + prem)
        next_res_06 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res_06 == previous_result:
            result_info.fx_NewVsLei_carab()
        else: sys.exit()
    def fx_MnuVsLei():
        print(away_vs_mnu + prem)
        next_res_05 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res_05 == previous_result:
            result_info.fx_LeiVsBou()
        else: sys.exit()
    def fx_LeiVsTot():
        print(home_vs_tot + prem)
        next_res_04 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res_04 == previous_result:
            result_info.fx_MnuVsLei()
        else: sys.exit()
    def fx_LutVsLei():
        print(away_vs_lut_carab + carab)
        next_res03 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res03 == previous_result:
            result_info.fx_LeiVsTot()
        else: sys.exit()
    def fx_LeiVsNew():
        print(home_vs_new + prem)
        next_res02 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res02 == previous_result:
            result_info.fx_LutVsLei()
        else: sys.exit()
    def fx_LivVsLei():
        print(away_vs_liv + prem)
        next_res01 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res01 == previous_result:
            result_info.fx_LeiVsNew()
        else: sys.exit()
    def fx_LeiVsBur():
        print(home_vs_bur + prem)
        next_res00 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res00 == previous_result:
            result_info.fx_LivVsLei()
        else: sys.exit()
    def fx_SouVsLei():
        print(away_vs_sou + prem)
        next_res10 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res10 == previous_result:
            result_info.fx_LeiVsBur()
        else: sys.exit()
    def fx_BtnVsLei():
        print(away_vs_btn + carab)
        next_res11 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res11 == previous_result:
            result_info.fx_SouVsLei()
        else: sys.exit()
    def fx_CryVsLei():
        print(away_vs_cry + prem)
        next_res12 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res12 == previous_result:
            result_info.fx_BtnVsLei()
        else: sys.exit()
    def fx_LeiVsArs():
        print(home_vs_ars + prem)
        next_res13 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res13 == previous_result:
            result_info.fx_CryVsLei()
        else: sys.exit()
    def fx_BhaVsLei():
        print(away_vs_bha + prem)
        next_res14 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res14 == previous_result:
            result_info.fx_LeiVsArs()
        else: sys.exit()
    def fx_LeiVsEve():
        print(home_vs_eve + prem)
        next_res15 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res15 == previous_result:
            result_info.fx_BhaVsLei()
        else: sys.exit()
    def fx_LeiVsWat():
        print(home_vs_wat + prem)
        next_res16 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res16 == previous_result:
            result_info.fx_LeiVsEve()
        else: sys.exit()
    def fx_AstVsLei():
        print(home_vs_ast + prem)
        next_res17 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res17 == previous_result:
            result_info.fx_LeiVsWat()
        else: sys.exit()
    def fx_LeiVsNor():
        print(home_vs_nor + prem)
        next_res18 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res18 == previous_result:
            result_info.fx_AstVsLei()
        else: sys.exit()
    def fx_MncVsLei():
        print(away_vs_mnc + prem)
        next_res19 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res19 == previous_result:
            result_info.fx_LeiVsNor()
        else: sys.exit()
    def fx_LeiVsLiv():
        print(home_vs_liv + prem)
        next_res20 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res20 == previous_result:
            result_info.fx_MncVsLei()
        else: sys.exit()
    def fx_WhuVsLei():
        print(away_vs_whu + prem)
        next_res21 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res21 == previous_result:
            result_info.fx_LeiVsLiv()
        else: sys.exit()
    def fx_NewVsLei():
        print(away_vs_new + prem)
        next_res22 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res22 == previous_result:
            result_info.fx_WhuVsLei()
        else: sys.exit()
    def fx_LeiVsSou():
        print(home_vs_sou + prem)
        next_res23 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res23 == previous_result:
            result_info.fx_NewVsLei()
        else: sys.exit()
    def fx_BurVsLei():
        print(away_vs_bur + prem)
        next_res24 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res24 == previous_result:
            result_info.fx_LeiVsSou()
        else: sys.exit()
    def fx_LeiVsWhu():
        print(home_vs_whu + prem)
        next_res25 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res25 == previous_result:
            result_info.fx_BurVsLei()
        else: sys.exit()
    def fx_LeiVsChe():
        print(home_vs_che + prem)
        next_res26 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res26 == previous_result:
            result_info.fx_LeiVsWhu()
        else: sys.exit()
    def fx_WolVsLei():
        print(away_vs_wol + prem)
        next_res27 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res27 == previous_result:
            result_info.fx_LeiVsChe()
        else: sys.exit()
    def fx_LeiVsMnc():
        print(home_vs_mnc + prem)
        next_res28 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res28 == previous_result:
            result_info.fx_WolVsLei()
        else: sys.exit()
    def fx_NorVsLei():
        print(away_vs_nor + prem)
        next_res29 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res29 == previous_result:
            result_info.fx_LeiVsMnc()
        else: sys.exit()
    def fx_LeiVsAst():
        print(home_vs_ast + prem)
        next_res30 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res30 == previous_result:
            result_info.fx_NorVsLei()
        else: sys.exit()
    def fx_WatVsLei():
        print(away_vs_wat + prem)
        next_res31 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res31 == previous_result:
            result_info.fx_LeiVsAst()
        else: sys.exit()
    def fx_LeiVsBha():
        print(home_vs_bha + prem)
        next_res32 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res32 == previous_result:
            result_info.fx_WatVsLei()
        else: sys.exit()
    def fx_EveVsLei():
        print(away_vs_eve + prem)
        next_res33 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res33 == previous_result:
            result_info.fx_LeiVsBha()
        else: sys.exit()
    def fx_LeiVsCry():
        print(home_vs_cry + prem)
        next_res34 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res34 == previous_result:
            result_info.fx_EveVsLei()
        else: sys.exit()
    def fx_ArsVsLei():
        print(away_vs_ars + prem)
        next_res35 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res35 == previous_result:
            result_info.fx_LeiVsCry()
        else: sys.exit()
    def fx_LeiVsShu():
        print(home_vs_shu + prem)
        next_res36 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res36 == previous_result:
            result_info.fx_ArsVsLei()
        else: sys.exit()
    def fx_TotVsLei():
        print(away_vs_tot + prem)
        next_res37 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res37 == previous_result:
            result_info.fx_LeiVsShu()
        else: sys.exit()
    def fx_LeiVsMnu():
        print(home_vs_mnu + prem)
        next_res38 = input('\n\nPress N for the next game or any other key to exit\n').lower()
        if next_res38 == previous_result:
            result_info.fx_TotVsLei()
        else: sys.exit()


latest_result_ident.leiVsBur()
