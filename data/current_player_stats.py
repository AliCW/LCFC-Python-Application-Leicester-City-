#v0.10
import sys

lcfc_squad = ('squad')
shut_down = str('exit')

sch_name = str('kasper schmeichel')
sch_initials = str('ks')

war_name = str('danny ward')
war_initials = str('dw')

jak_name = str('eldin jakupovic')
jak_initials = str('ej')

jus_name = str('james justin')
jus_initials = str('jj')

chi_name = str('ben chilwell')
chi_initials = str('bc')

soy_name = str('caglar soyuncu')
soy_initials = str('cs')

mor_name = str('wes morgan')
mor_initials = str('wm')

eva_name = str('jonny evans')
eva_initials = str('je')

ben_name = str('filip benkovic')
ben_initials = str('fb')

ama_name = str('daniel amartey')
ama_initials = str('da')

rper_name = str('ricardo pereira')
rper_initials = str('rp')

fuc_name = str('christian fuchs')
fuc_initials = str('cf')

gra_name = str('demarai gray')
gra_initials = str('dg')

tie_name = str('youri tielemans')
tie_initials = str('yt')

mad_name = str('james maddison')
mad_initials = str('jm')

alb_name = str('marc albrighton')
alb_initials = str('ma')

bar_name = str('harvey barnes')
bar_initials = str('hb')

cho_name = str('hamza choudhury')
cho_initials = str('hc')

jam_name = str('matty james')
jam_initials = str('mj')

men_name = str('nampalys mendy')
men_initials = str('nm')

ndi_name = str('wilfred ndidi')
ndi_initials = str('wn')

pra_name = str('dennis praet')
pra_initials = str('dp')

var_name = str('jamie vardy')
var_initials = str('jv')

ihe_name = str('kelechi iheanacho')
ihe_initials = ('ki')

per_name = str('ayoze perez')
per_initials = str('ap')

#GOALKEEPER<-------------------------------------------------------------------------------------------------------
#Kasper Schmeichel<-------------https://www.lcfc.com/players/2508/Kasper-Schmeichel/profile?tabs=Statistics
sch_nation = str('Danish')
sch_saves = str(35)
sch_punches = str(3)#basic_stats
sch_high_claims = str(8)
sch_catches = str(5)
sch_sweeps = str(5)
sch_throw_outs = str(71)
sch_goal_kicks = str(119)
sch_clean_sheets = str(7)
sch_goals_conceded = str(10)

sch_assists = str(0)#team_play
sch_passes_completed = str(294)
sch_passes_per_game = str(26)
sch_pass_accuracy = str(75)

sch_appearances = str(16)#performance_stats
sch_total_saves = str(35)
sch_saves_per_game = str(2.2)
sch_wins = str(12)
sch_draws = str(2)
sch_losses = str(2)

sch_yellow_cards = str(0)#discipline_stats
sch_red_cards = str(0)
sch_fouls = str(0)
#Danny Ward<--------------- https://www.lcfc.com/players/4522/Danny-Ward/profile?tabs=Statistics
war_nation = str('Welsh')
war_saves = str(0)
war_punches = str(0)#basic_stats
war_high_claims = str(0)
war_catches = str(0)
war_sweeps = str(0)
war_throw_outs = str(0)
war_goal_kicks = str(0)
war_clean_sheets = str(0)
war_goals_conceded = str(0)

war_assists = str(0)#team_play
war_passes_completed = str(0)
war_passes_per_game = str(0)
war_pass_accuracy = str(0)

war_appearances = str(0)#performance_stats
war_total_saves = str(0)
war_saves_per_game = str(0)
war_wins = str(0)
war_draws = str(0)
war_losses = str(0)

war_yellow_cards = str(0)#discipline_stats
war_red_cards = str(0)
war_fouls = str(0)

#Eldin Jakupovic<--------------https://www.lcfc.com/players/4786/Eldin-Jakupovic/profile?tabs=Statistics
jak_nation = str('Swiss')
jak_saves = str(0)
jak_punches = str(0)#basic_stats
jak_high_claims = str(0)
jak_catches = str(0)
jak_sweeps = str(0)
jak_throw_outs = str(0)
jak_goal_kicks = str(0)
jak_clean_sheets = str(0)
jak_goals_conceded = str(0)

jak_assists = str(0) #team_play
jak_passes_completed = str(0)
jak_passes_per_game = str(0)
jak_pass_accuracy = str(0)

jak_appearances = str(0)#performance_stats
jak_total_saves = str(0)
jak_saves_per_game = str(0)
jak_wins = str(0)
jak_draws = str(0)
jak_losses = str(0)

jak_yellow_cards = str(0)#discipline_stats
jak_red_cards = str(0)
jak_fouls = str(0)

#DEFENCE<---------------------------------------------------------------------------------------------------------------
# James Justin stats<------https://www.lcfc.com/players/13515/James-Justin/profile?tabs=Statistics
jus_nation = str('English')
jus_appearances = str(2) #appearances
jus_goals = str(0) #goals
jus_tackles = str(1) #tackles made
jus_intercept = str(0) #interceptions made
jus_clean_sheets = str(0)#clean sheets

jus_yellow_cards = str(0)
jus_red_cards = str(0)
jus_fouls = str(0)
jus_offside = str(0)

# Ben Chilwell stats<--------https://www.lcfc.com/players/13491/Ben-Chilwell/profile?tabs=Statistics
chi_nation = str('English')
chi_appearances = str(13) #appearances
chi_goals = str(1) #goals
chi_tackles = str(18) #tackles made
chi_intercept = str(13) #interceptions made
chi_clean_sheets = str(6)#clean sheets

chi_yellow_cards = str(1)
chi_red_cards = str(0)
chi_fouls = str(12)
chi_offside = str(0)

#Caglar Soyuncu stats<---------https://www.lcfc.com/players/26216/%C3%87aglar-S%C3%B6y%C3%BCnc%C3%BC/profile?tabs=Statistics
soy_nation = str('Turkish')
soy_appearances = str(16) #appearances
soy_goals = str(1) #goals
soy_tackles = str(28) #tackles made
soy_intercept = str(23) #interceptions made
soy_clean_sheets = str(7)#clean sheets

soy_yellow_cards = str(3)
soy_red_cards = str(0)
soy_fouls = str(14)
soy_offside = str(1)

#Wes Morgan stats<----------https://www.lcfc.com/players/8966/Wes-Morgan/profile?tabs=Statistics
mor_nation = str('Jamaican')
mor_appearances = str(4) #appearances
mor_goals = str(0) #goals
mor_tackles = str(0) #tackles made
mor_intercept = str(0) #interceptions made
mor_clean_sheets = str(0)#clean sheets

mor_yellow_cards = str(0)
mor_red_cards = str(0)
mor_fouls = str(1)
mor_offside = str(0)

#Jonny Evans stats<---------https://www.lcfc.com/players/3156/Jonny-Evans/profile?tabs=Statistics
eva_nation = str('Northern Irish')
eva_appearances = str(16) #appearances
eva_goals = str(1) #goals
eva_tackles = str(20) #tackles made
eva_intercept = str(21) #interceptions made
eva_clean_sheets = str(6)#clean sheets

eva_yellow_cards = str(3)
eva_red_cards = str(0)
eva_fouls = str(4)
eva_offside = str(0)

#Filip Benkovic<---------https://www.lcfc.com/players/16671/Filip-Benkovic/profile?tabs=Statistics
ben_nation = str('Croatian')
ben_appearances = str(0) #appearances
ben_goals = str(0) #goals
ben_tackles = str(0) #tackles made
ben_intercept = str(0) #interceptions made
ben_clean_sheets = str(0)#clean sheets

ben_yellow_cards = str(0)
ben_red_cards = str(0)
ben_fouls = str(0)
ben_offside = str(0)

#Daniel Amartey<----------https://www.lcfc.com/players/12306/Daniel-Amartey/profile?tabs=Statistics
ama_nation = str('Ghanaian')
ama_appearances = str(0) #appearances
ama_goals = str(0) #goals
ama_tackles = str(0) #tackles made
ama_intercept = str(0) #interceptions made
ama_clean_sheets = str(0)#clean sheets

ama_yellow_cards = str(0)
ama_red_cards = str(0)
ama_fouls = str(0)
ama_offside = str(0)

#Ricardo Pereira<-----------https://www.lcfc.com/players/5343/Ricardo-Pereira/profile?tabs=Statistics
rper_nation = str('Portuguese')
rper_appearances = str(16) #appearances
rper_goals = str(2) #goals
rper_tackles = str(70) #tackles made
rper_intercept = str(31) #interceptions made
rper_clean_sheets = str(7)#clean sheets

rper_yellow_cards = str(1)
rper_red_cards = str(0)
rper_fouls = str(25)
rper_offside = str(0)

#Christian Fuchs<------------https://www.lcfc.com/players/5371/Christian-Fuchs/profile?tabs=Statistics
fuc_nation = str('Austria')
fuc_appearances = str(4) #appearances
fuc_goals = str(0) #goals
fuc_tackles = str(9) #tackles made
fuc_intercept = str(2) #interceptions made
fuc_clean_sheets = str(1)#clean sheets

fuc_yellow_cards = str(0)
fuc_red_cards = str(0)
fuc_fouls = str(1)
fuc_offside = str(1)

#MIDFIELD<--------------------------------------------------------------------------------
#Demarai Gray https://www.lcfc.com/players/7946/Demarai-Gray/profile?tabs=Statistics
gra_nation = str('English')
gra_appearances = str(9) #appearances
gra_goals = str(0) #goals
gra_passes = str(90)#passes
gra_passes_tar = str(81) #passes on target
gra_shots = str(5) #shots
gra_shots_tar = str(3) #shots on target
gra_assists = str(1) #

gra_yellow_cards = str(1)
gra_red_cards = str(0)
gra_fouls = str(1)
gra_offside = str(2)

#Youri Tielemans  https://www.lcfc.com/players/5865/Youri-Tielemans/profile?tabs=Statistics
tie_nation = str('Belgian')
tie_appearances = str(16) #appearances
tie_goals = str(3) #goals
tie_passes = str(872)#passes
tie_passes_tar = str(716) #passes on target
tie_shots = str(32) #shots
tie_shots_tar = str(6) #shots on target
tie_assists = str(3) #

tie_yellow_cards = str(0)
tie_red_cards = str(0)
tie_fouls = str(13)
tie_offside = str(1)

#James Maddison   https://www.lcfc.com/players/8456/James-Maddison/profile?tabs=Statistics
mad_nation = str('English')
mad_appearances = str(15) #appearances
mad_goals = str(5) #goals
mad_passes = str(751)#passes
mad_passes_tar = str(631) #passes on target
mad_shots = str(42) #shots
mad_shots_tar = str(10) #shots on target
mad_assists = str(3) #

mad_yellow_cards = str(1)
mad_red_cards = str(0)
mad_fouls = str(18)
mad_offside = str(2)

#Marc Albighton https://www.lcfc.com/players/3564/Marc-Albrighton/profile?tabs=Statistics
alb_nation = str('English')
alb_appearances = str(8) #appearances
alb_goals = str(0) #goals
alb_passes = str(128)#passes
alb_passes_tar = str(101) #passes on target
alb_shots = str(4) #shots
alb_shots_tar = str(1) #shots on target
alb_assists = str(1) #

alb_yellow_cards = str(1)
alb_red_cards = str(0)
alb_fouls = str(4)
alb_offside = str(1)

#Harvey Barnes https://www.lcfc.com/players/14716/Harvey-Barnes/profile?tabs=Statistics
bar_nation = str('English')
bar_appearances = str(15) #appearances
bar_goals = str(1) #goals
bar_passes = str(306)#passes
bar_passes_tar = str(241) #passes on target
bar_shots = str(27) #shots
bar_shots_tar = str(12) #shots on target
bar_assists = str(4) #

bar_yellow_cards = str(0)
bar_red_cards = str(0)
bar_fouls = str(13)
bar_offside = str(0)

#Hamza Choudhury https://www.lcfc.com/players/13248/Hamza-Choudhury/profile?tabs=Statistics
cho_nation = str('English')
cho_appearances = str(9) #appearances
cho_goals = str(0) #goals
cho_passes = str(200)#passes
cho_passes_tar = str(174) #passes on target
cho_shots = str(3) #shots
cho_shots_tar = str(1) #shots on target
cho_assists = str(1) #

cho_yellow_cards = str(1)
cho_red_cards = str(0)
cho_fouls = str(4)
cho_offside = str(0)

#Matty James https://www.lcfc.com/players/3669/Matty-James/profile?tabs=Statistics
jam_nation = str('English')
jam_appearances = str(0) #appearances
jam_goals = str(0) #goals
jam_passes = str(0)#passes
jam_passes_tar = str(0) #passes on target
jam_shots = str(0) #shots
jam_shots_tar = str(0) #shots on target
jam_assists = str(0) #

jam_yellow_cards = str(0)
jam_red_cards = str(0)
jam_fouls = str(0)
jam_offside = str(0)

#Nampalys Mendy https://www.lcfc.com/players/19617/Nampalys-Mendy/profile?tabs=Statistics
men_nation = str('French')
men_appearances = str(1) #appearances
men_goals = str(0) #goals
men_passes = str(3)#passes
men_passes_tar = str(1) #passes on target
men_shots = str(0) #shots
men_shots_tar = str(0) #shots on target
men_assists = str(0) #

men_yellow_cards = str(0)
men_red_cards = str(0)
men_fouls = str(1)
men_offside = str(0)

#Wilfred Ndidi https://www.lcfc.com/players/20479/Wilfred-Ndidi/profile?tabs=Statistics
ndi_nation = str('Nigerian')
ndi_appearances = str(15) #appearances
ndi_goals = str(2) #goals
ndi_passes = str(793)#passes
ndi_passes_tar = str(666) #passes on target
ndi_shots = str(13) #shots
ndi_shots_tar = str(3) #shots on target
ndi_assists = str(0) #

ndi_yellow_cards = str(2)
ndi_red_cards = str(0)
ndi_fouls = str(23)
ndi_offside = str(1)

#Dennis Praet https://www.lcfc.com/players/5860/Dennis-Praet/profile?tabs=Statistics
pra_nation = str('Belgian')
pra_appearances = str(11) #appearances
pra_goals = str(0) #goals
pra_passes = str(215)#passes
pra_passes_tar = str(183) #passes on target
pra_shots = str(6) #shots
pra_shots_tar = str(0) #shots on target
pra_assists = str(1) #

pra_yellow_cards = str(0)
pra_red_cards = str(0)
pra_fouls = str(9)
pra_offside = str(0)

#FORWARD<-------------------------------------------------------------------------------------------
#key stats https://www.lcfc.com/players/8979/Jamie-Vardy/profile?tabs=Statistics
var_nation = str('English')
var_appearances = str(16) #appearances
var_goals = str(16) #goals
var_left = str(6)#goals with left foot
var_right = str(7)#goals with right foot
var_headers = str(3)#goals with header
var_fkick = str(0)#goals from free kicks
var_pen = str(3)#goals from penalties
var_shots = str(41) #shots
var_shots_tar = str(26) #shots on target
var_assists = str(3) #

var_yellow_cards = str(2)
var_red_cards = str(0)
var_fouls = str(13)
var_offside = str(14)

#key stats https://www.lcfc.com/players/13554/Kelechi-Iheanacho/profile?tabs=Statistics
ihe_nation = str('Nigerian')
ihe_appearances = str(2) #appearances
ihe_goals = str(2) #goals
ihe_left = str(1)#goals with left foot
ihe_right = str(1)#goals with right foot
ihe_headers = str(0)#goals with header
ihe_fkick = str(0)#goals from free kicks
ihe_pen = str(0)#goals from penalties
ihe_shots = str(7) #shots
ihe_shots_tar = str(3) #shots on target
ihe_assists = str(2) #

ihe_yellow_cards = str(1)
ihe_red_cards = str(0)
ihe_fouls = str(1)
ihe_offside = str(2)

#key stats https://www.lcfc.com/players/10487/Ayoze-P%C3%A9rez/profile?tabs=Statistics
per_nation = str('Spanish')
per_appearances = str(14) #appearances
per_goals = str(4) #goals
per_left = str(1)#goals with left foot
per_right = str(3)#goals with right foot
per_headers = str(0)#goals with header
per_fkick = str(0)#goals from free kicks
per_pen = str(0)#goals from penalties
per_shots = str(22) #shots
per_shots_tar = str(11) #shots on target
per_assists = str(1) #

per_yellow_cards = str(0)
per_red_cards = str(0)
per_fouls = str(11)
per_offside = str(2)

#User query switch<-------------------------------------------------------------------------------
def start_player_stats_query(): #Code for the user query positioned on startup
    starter_user_query = input('\nType the name or initials of the player, or "squad" to see the team list '
                               'or "exit" to close\n[All player statistics are in relation to the premier league]\n').lower()
    if (starter_user_query == lcfc_squad):
        list_squad()
        start_player_stats_query()
    if (starter_user_query == shut_down):
        sys.exit()
    if (starter_user_query == sch_name) or (starter_user_query == sch_initials): #Schmeichel
        sch_basic_stats()
        sch_team_play()
        sch_performance_stats()
        sch_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == war_name) or (starter_user_query == war_initials): #Ward
        war_basic_stats()
        war_team_play()
        war_performance_stats()
        war_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == jak_name) or (starter_user_query == jak_initials): #Jakupovic
        jak_basic_stats()
        jak_team_play()
        jak_performance_stats()
        jak_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == jus_name) or (starter_user_query == jus_initials): #Justin
        jus_key_stats()
        jus_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == chi_name) or (starter_user_query == chi_initials): #Chilwell
        chi_key_stats()
        chi_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == soy_name) or (starter_user_query == soy_initials): #Soyuncu
        soy_key_stats()
        soy_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == mor_name) or (starter_user_query == mor_initials): #Morgan
        mor_key_stats()
        mor_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == eva_name) or (starter_user_query == eva_initials): #Evans
        eva_key_stats()
        eva_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ben_name) or (starter_user_query == ben_initials): #Benkovic
        ben_key_stats()
        ben_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ama_name) or (starter_user_query == ama_initials): #Amartey
        ama_key_stats()
        ama_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == rper_name) or (starter_user_query == rper_initials): #Pereira
        rper_key_stats()
        rper_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == fuc_name) or (starter_user_query == fuc_initials): #Fuchs
        fuc_key_stats()
        fuc_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == gra_name) or (starter_user_query == gra_initials): #Gray
        gra_key_stats()
        gra_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == tie_name) or (starter_user_query == tie_initials): #Tielemans
        tie_key_stats()
        tie_discipline_stats()
    if (starter_user_query == mad_name) or (starter_user_query == mad_initials): #Maddison
        mad_key_stats()
        mad_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == alb_name) or (starter_user_query == alb_initials): #Albrighton
        alb_key_stats()
        alb_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == bar_name) or (starter_user_query == bar_initials): #Barnes
        bar_key_stats()
        bar_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == cho_name) or (starter_user_query == cho_initials): #Choudhury
        cho_key_stats()
        cho_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == jam_name) or (starter_user_query == jam_initials): #James
        jam_key_stats()
        jam_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == men_name) or (starter_user_query == men_initials): #Mendy
        men_key_stats()
        men_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ndi_name) or (starter_user_query == ndi_initials): #Ndidi
        ndi_key_stats()
        ndi_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == pra_name) or (starter_user_query == pra_initials): #Praet
        pra_key_stats()
        pra_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == var_name) or (starter_user_query == var_initials): #Vardy
        var_key_stats()
        var_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ihe_name) or (starter_user_query == ihe_initials): #Iheanacho
        ihe_key_stats()
        ihe_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == per_name) or (starter_user_query == per_initials): #Perez
        per_key_stats()
        per_discipline_stats()
        start_player_stats_query()
    else: player_syntax_fail()
        
def player_syntax_fail():
    print('\nUnknown player / initials, try again or use "squad" for a full list\n')
    start_player_stats_query()

#Squad print definition<------------------------------------------------------------------------
def list_squad():
    print('\nGoalkeepers:')
    print(sch_name + ' - ' + sch_initials + ' | ' + war_name + ' - ' + war_initials + ' | ' + jak_name + ' - ' + jak_initials)
    print('\nDefense:')
    print(jus_name + ' - ' + jus_initials + ' | ' + chi_name + ' - ' + chi_initials + ' | ' + soy_name + ' - ' + soy_initials)
    print(mor_name + ' - ' + mor_initials + ' | ' + eva_name + ' - ' + eva_initials + ' | ' + ben_name + ' - ' + ben_initials)
    print(ama_name + ' - ' + ama_initials + ' | ' + rper_name + ' - ' + rper_initials + ' | ' + fuc_name + ' - ' + fuc_initials)
    print('\nMidfield:')
    print(gra_name + ' - ' + gra_initials + ' | ' + tie_name + ' - ' + tie_initials + ' | ' + mad_name + ' - ' + mad_initials)
    print(alb_name + ' - ' + alb_initials + ' | ' + bar_name + ' - ' + bar_initials + ' | ' + cho_name + ' - ' + cho_initials)
    print(jam_name + ' - ' + jam_initials + ' | ' + men_name + ' - ' + men_initials + ' | ' + ndi_name + ' - ' + ndi_initials)
    print(pra_name + ' - ' + pra_initials)
    print('\nForwards')
    print(var_name + ' - ' + var_initials + ' | ' + ihe_name + ' - ' + ihe_initials + ' | ' + per_name + ' - ' + per_initials)


#Player print definitions
#Kasper Schmeichel print defintions<-------------------------------------------------------------
def sch_basic_stats():
    print('Kasper Schmeichel')
    print('Nationality:     ' + sch_nation)
    print('Saves:           ' + sch_saves)
    print('Punches:         ' + sch_punches)
    print('High Claims:     ' + sch_high_claims)
    print('Catches:         ' + sch_catches)
    print('Sweeps:          ' + sch_sweeps)
    print('Throw Outs:      ' + sch_throw_outs)
    print('Goal Kicks:      ' + sch_goal_kicks)
    print('Clean Sheets:    ' + sch_clean_sheets)
    print('Conceded:        ' + sch_goals_conceded)
def sch_team_play():
    print('\nAssists:           ' + sch_assists)
    print('Passes Completed:    ' + sch_passes_completed)
    print('Passes Per Game:     ' + sch_passes_per_game)
    print('Pass Accuracy:       ' + sch_pass_accuracy + '%\n')
def sch_performance_stats():
    print('Appearances:     ' + sch_appearances)
    print('Total Saves:     ' + sch_total_saves)
    print('Saves Per Game:  ' + sch_saves_per_game)
    print('Wins:            ' + sch_wins)
    print('Draws:           ' + sch_draws)
    print('Losses:          ' + sch_losses)
def sch_discipline_stats():
    print('Fouls:           ' + sch_fouls)
    print('Yellow Cards:    ' + sch_yellow_cards)
    print('Red Cards:       ' + sch_red_cards)
#Danny Ward print definition<-------------------------------------------------------------
def war_basic_stats():
    print('Danny Ward')
    print('Nationality:     ' + war_nation)
    print('Saves:           ' + war_saves)
    print('Punches:         ' + war_punches)
    print('High Claims:     ' + war_high_claims)
    print('Catches:         ' + war_catches)
    print('Sweeps:          ' + war_sweeps)
    print('Throw Outs:      ' + war_throw_outs)
    print('Goal Kicks:      ' + war_goal_kicks)
    print('Clean Sheets:    ' + war_clean_sheets)
    print('Conceded:        ' + war_goals_conceded)
def war_team_play():
    print('\nAssists:           ' + war_assists)
    print('Passes Completed:    ' + war_passes_completed)
    print('Passes Per Game:     ' + war_passes_per_game)
    print('Pass Accuracy:       ' + war_pass_accuracy + '%\n')
def war_performance_stats():
    print('Appearances:     ' + war_appearances)
    print('Total Saves:     ' + war_total_saves)
    print('Saves Per Game:  ' + war_saves_per_game)
    print('Wins:            ' + war_wins)
    print('Draws:           ' + war_draws)
    print('Losses:          ' + war_losses)
def war_discipline_stats():
    print('Fouls:           ' + war_fouls)
    print('Yellow Cards:    ' + war_yellow_cards)
    print('Red Cards:       ' + war_red_cards)

#Eldin Jakupovic print definitions<-------------------------------------------------------------
def jak_basic_stats():
    print('Eldin Jakupovic')
    print('Nationality:     ' + jak_nation)
    print('Saves:           ' + jak_saves)
    print('Punches:         ' + jak_punches)
    print('High Claims:     ' + jak_high_claims)
    print('Catches:         ' + jak_catches)
    print('Sweeps:          ' + jak_sweeps)
    print('Throw Outs:      ' + jak_throw_outs)
    print('Goal Kicks:      ' + jak_goal_kicks)
    print('Clean Sheets:    ' + jak_clean_sheets)
    print('Conceded:        ' + jak_goals_conceded)
def jak_team_play():
    print('\nAssists:           ' + jak_assists)
    print('Passes Completed:    ' + jak_passes_completed)
    print('Passes Per Game:     ' + jak_passes_per_game)
    print('Pass Accuracy:       ' + jak_pass_accuracy + '%\n')
def jak_performance_stats():
    print('Appearances:     ' + jak_appearances)
    print('Total Saves:     ' + jak_total_saves)
    print('Saves Per Game:  ' + jak_saves_per_game)
    print('Wins:            ' + jak_wins)
    print('Draws:           ' + jak_draws)
    print('Losses:          ' + jak_losses)
def jak_discipline_stats():
    print('Fouls:           ' + jak_fouls)
    print('Yellow Cards:    ' + jak_yellow_cards)
    print('Red Cards:       ' + jak_red_cards)

# James Justin <-------------------------------------------------------
def jus_key_stats():
    print('James Justin')
    print('Nationality:         ' + jus_nation)
    print('Appearances:         ' + jus_appearances)
    print('Goals:               ' + jus_goals)
    print('Tackles:             ' + jus_tackles)
    print('Interceptions:       ' + jus_intercept)
    print('Clean Sheets:        ' + jus_clean_sheets)
def jus_discipline_stats():
    print('Offsides:            ' + jus_yellow_cards)
    print('Fouls:               ' + jus_fouls)
    print('Yellow cards:        ' + jus_yellow_cards)
    print('Red Cards:           ' + jus_red_cards)

# Ben Chilwell <-------------------------------------------------------
def chi_key_stats():
    print('Ben Chilwell')
    print('Nationality:         ' + chi_nation)
    print('Appearances:         ' + chi_appearances)
    print('Goals:               ' + chi_goals)
    print('Tackles:             ' + chi_tackles)
    print('Interceptions:       ' + chi_intercept)
    print('Clean Sheets:        ' + chi_clean_sheets)
def chi_discipline_stats():
    print('Offsides:            ' + chi_yellow_cards)
    print('Fouls:               ' + chi_fouls)
    print('Yellow cards:        ' + chi_yellow_cards)
    print('Red Cards:           ' + chi_red_cards)

# Caglar Soyuncu stats<------------------------------------------------
def soy_key_stats():
    print('Caglar Soyuncu')
    print('Nationality:         ' + soy_nation)
    print('Appearances:         ' + soy_appearances)
    print('Goals:               ' + soy_goals)
    print('Tackles:             ' + soy_tackles)
    print('Interceptions:       ' + soy_intercept)
    print('Clean Sheets:        ' + soy_clean_sheets)
def soy_discipline_stats():
    print('Offsides:            ' + soy_yellow_cards)
    print('Fouls:               ' + soy_fouls)
    print('Yellow cards:        ' + soy_yellow_cards)
    print('Red Cards:           ' + soy_red_cards)

# Wes Morgan stats<------------------------------------------------------
def mor_key_stats():
    print('Wes Morgan')
    print('Nationality:         ' + mor_nation)
    print('Appearances:         ' + mor_appearances)
    print('Goals:               ' + mor_goals)
    print('Tackles:             ' + mor_tackles)
    print('Interceptions:       ' + mor_intercept)
    print('Clean Sheets:        ' + mor_clean_sheets)
def mor_discipline_stats():
    print('Offsides:            ' + mor_yellow_cards)
    print('Fouls:               ' + mor_fouls)
    print('Yellow cards:        ' + mor_yellow_cards)
    print('Red Cards:           ' + mor_red_cards)

# Jonny Evans stats<-------------------------------------------------------
def eva_key_stats():
    print('Jonny Evans')
    print('Nationality:         ' + eva_nation)
    print('Appearances:         ' + eva_appearances)
    print('Goals:               ' + eva_goals)
    print('Tackles:             ' + eva_tackles)
    print('Interceptions:       ' + eva_intercept)
    print('Clean Sheets:        ' + eva_clean_sheets)
def eva_discipline_stats():
    print('Offsides:            ' + eva_yellow_cards)
    print('Fouls:               ' + eva_fouls)
    print('Yellow cards:        ' + eva_yellow_cards)
    print('Red Cards:           ' + eva_red_cards)

# Filip Benkovic<--------------------------------------------------------
def ben_key_stats():
    print('Filip Benkovic')
    print('Nationality:         ' + ben_nation)
    print('Appearances:         ' + ben_appearances)
    print('Goals:               ' + ben_goals)
    print('Tackles:             ' + ben_tackles)
    print('Interceptions:       ' + ben_intercept)
    print('Clean Sheets:        ' + ben_clean_sheets)
def ben_discipline_stats():
    print('Offsides:            ' + ben_yellow_cards)
    print('Fouls:               ' + ben_fouls)
    print('Yellow cards:        ' + ben_yellow_cards)
    print('Red Cards:           ' + ben_red_cards)

# Daniel Amartey<----------------------------------------------------------
def ama_key_stats():
    print('Daniel Amartey')
    print('Nationality:         ' + ama_nation)
    print('Appearances:         ' + ama_appearances)
    print('Goals:               ' + ama_goals)
    print('Tackles:             ' + ama_tackles)
    print('Interceptions:       ' + ama_intercept)
    print('Clean Sheets:        ' + ama_clean_sheets)
def ama_discipline_stats():
    print('Offsides:            ' + ama_yellow_cards)
    print('Fouls:               ' + ama_fouls)
    print('Yellow cards:        ' + ama_yellow_cards)
    print('Red Cards:           ' + ama_red_cards)

# Ricardo Pereira<--------------------------------------------------------
def rper_key_stats():
    print('Ricardo Pereira')
    print('Nationality:         ' + rper_nation)
    print('Appearances:         ' + rper_appearances)
    print('Goals:               ' + rper_goals)
    print('Tackles:             ' + rper_tackles)
    print('Interceptions:       ' + rper_intercept)
    print('Clean Sheets:        ' + rper_clean_sheets)
def rper_discipline_stats():
    print('Offsides:            ' + rper_yellow_cards)
    print('Fouls:               ' + rper_fouls)
    print('Yellow cards:        ' + rper_yellow_cards)
    print('Red Cards:           ' + rper_red_cards)

# Christian Fuchs<----------------------------------------------------------
def fuc_key_stats():
    print('Christian Fuchs')
    print('Nationality:         ' + fuc_nation)
    print('Appearances:         ' + fuc_appearances)
    print('Goals:               ' + fuc_goals)
    print('Tackles:             ' + fuc_tackles)
    print('Interceptions:       ' + fuc_intercept)
    print('Clean Sheets:        ' + fuc_clean_sheets)
def fuc_discipline_stats():
    print('Offsides:            ' + fuc_yellow_cards)
    print('Fouls:               ' + fuc_fouls)
    print('Yellow cards:        ' + fuc_yellow_cards)
    print('Red Cards:           ' + fuc_red_cards)

#Midfield Print definitions<-------------------------------------------------------------------------------
#Demarai Gray print defintions<-------------------------------------------------------------
def gra_key_stats():
    print('Demarai Gray')
    print('Nationality:         ' + gra_nation)
    print('Appearances:         ' + gra_appearances)
    print('Goals:               ' + gra_goals)
    print('Passes:              ' + gra_passes)
    print('Passes on target:    ' + gra_passes_tar)
    print('Shots:               ' + gra_shots)
    print('Shots on target:     ' + gra_shots_tar)
    print('Assists:             ' + gra_assists)
def gra_discipline_stats():
    print('Offsides:            ' + gra_yellow_cards)
    print('Fouls:               ' + gra_fouls)
    print('Yellow cards:        ' + gra_yellow_cards)
    print('Red Cards:           ' + gra_red_cards)

#Youri Tielemans print defintions<-------------------------------------------------------------
def tie_key_stats():
    print('Youri Tielemans')
    print('Nationality:         ' + tie_nation)
    print('Appearances:         ' + tie_appearances)
    print('Goals:               ' + tie_goals)
    print('Passes:              ' + tie_passes)
    print('Passes on target:    ' + tie_passes_tar)
    print('Shots:               ' + tie_shots)
    print('Shots on target:     ' + tie_shots_tar)
    print('Assists:             ' + tie_assists)
def tie_discipline_stats():
    print('Offsides:            ' + tie_yellow_cards)
    print('Fouls:               ' + tie_fouls)
    print('Yellow cards:        ' + tie_yellow_cards)
    print('Red Cards:           ' + tie_red_cards)

#James Maddison print defintions<-------------------------------------------------------------
def mad_key_stats():
    print('James Maddison')
    print('Nationality:         ' + mad_nation)
    print('Appearances:         ' + mad_appearances)
    print('Goals:               ' + mad_goals)
    print('Passes:              ' + mad_passes)
    print('Passes on target:    ' + mad_passes_tar)
    print('Shots:               ' + mad_shots)
    print('Shots on target:     ' + mad_shots_tar)
    print('Assists:             ' + mad_assists)
def mad_discipline_stats():
    print('Offsides:            ' + mad_yellow_cards)
    print('Fouls:               ' + mad_fouls)
    print('Yellow cards:        ' + mad_yellow_cards)
    print('Red Cards:           ' + mad_red_cards)

#Marc Albrighton print defintions<-------------------------------------------------------------
def alb_key_stats():
    print('Marc Albrighton')
    print('Nationality:         ' + alb_nation)
    print('Appearances:         ' + alb_appearances)
    print('Goals:               ' + alb_goals)
    print('Passes:              ' + alb_passes)
    print('Passes on target:    ' + alb_passes_tar)
    print('Shots:               ' + alb_shots)
    print('Shots on target:     ' + alb_shots_tar)
    print('Assists:             ' + alb_assists)
def alb_discipline_stats():
    print('Offsides:            ' + alb_yellow_cards)
    print('Fouls:               ' + alb_fouls)
    print('Yellow cards:        ' + alb_yellow_cards)
    print('Red Cards:           ' + alb_red_cards)

#Harvey Barnes print defintions<-------------------------------------------------------------
def bar_key_stats():
    print('Harvey Barnes')
    print('Nationality:         ' + bar_nation)
    print('Appearances:         ' + bar_appearances)
    print('Goals:               ' + bar_goals)
    print('Passes:              ' + bar_passes)
    print('Passes on target:    ' + bar_passes_tar)
    print('Shots:               ' + bar_shots)
    print('Shots on target:     ' + bar_shots_tar)
    print('Assists:             ' + bar_assists)
def bar_discipline_stats():
    print('Offsides:            ' + bar_yellow_cards)
    print('Fouls:               ' + bar_fouls)
    print('Yellow cards:        ' + bar_yellow_cards)
    print('Red Cards:           ' + bar_red_cards)

#Hamza Choudhury print defintions<-------------------------------------------------------------
def cho_key_stats():
    print('Hamza Choudhury')
    print('Nationality:         ' + cho_nation)
    print('Appearances:         ' + cho_appearances)
    print('Goals:               ' + cho_goals)
    print('Passes:              ' + cho_passes)
    print('Passes on target:    ' + cho_passes_tar)
    print('Shots:               ' + cho_shots)
    print('Shots on target:     ' + cho_shots_tar)
    print('Assists:             ' + cho_assists)
def cho_discipline_stats():
    print('Offsides:            ' + cho_yellow_cards)
    print('Fouls:               ' + cho_fouls)
    print('Yellow cards:        ' + cho_yellow_cards)
    print('Red Cards:           ' + cho_red_cards)

#Matty James print defintions<-------------------------------------------------------------
def jam_key_stats():
    print('Matty James')
    print('Nationality:         ' + jam_nation)
    print('Appearances:         ' + jam_appearances)
    print('Goals:               ' + jam_goals)
    print('Passes:              ' + jam_passes)
    print('Passes on target:    ' + jam_passes_tar)
    print('Shots:               ' + jam_shots)
    print('Shots on target:     ' + jam_shots_tar)
    print('Assists:             ' + jam_assists)
def jam_discipline_stats():
    print('Offsides:            ' + jam_yellow_cards)
    print('Fouls:               ' + jam_fouls)
    print('Yellow cards:        ' + jam_yellow_cards)
    print('Red Cards:           ' + jam_red_cards)

#Nampalys Mendy print defintions<-------------------------------------------------------------
def men_key_stats():
    print('Nampalys Mendy')
    print('Nationality:         ' + men_nation)
    print('Appearances:         ' + men_appearances)
    print('Goals:               ' + men_goals)
    print('Passes:              ' + men_passes)
    print('Passes on target:    ' + men_passes_tar)
    print('Shots:               ' + men_shots)
    print('Shots on target:     ' + men_shots_tar)
    print('Assists:             ' + men_assists)
def men_discipline_stats():
    print('Offsides:            ' + men_yellow_cards)
    print('Fouls:               ' + men_fouls)
    print('Yellow cards:        ' + men_yellow_cards)
    print('Red Cards:           ' + men_red_cards)

#Wilfred Ndidi print defintions<-------------------------------------------------------------
def ndi_key_stats():
    print('Wilfred Ndidi')
    print('Nationality:         ' + ndi_nation)
    print('Appearances:         ' + ndi_appearances)
    print('Goals:               ' + ndi_goals)
    print('Passes:              ' + ndi_passes)
    print('Passes on target:    ' + ndi_passes_tar)
    print('Shots:               ' + ndi_shots)
    print('Shots on target:     ' + ndi_shots_tar)
    print('Assists:             ' + ndi_assists)
def ndi_discipline_stats():
    print('Offsides:            ' + ndi_yellow_cards)
    print('Fouls:               ' + ndi_fouls)
    print('Yellow cards:        ' + ndi_yellow_cards)
    print('Red Cards:           ' + ndi_red_cards)

#Dennis Praet print defintions<-------------------------------------------------------------
def pra_key_stats():
    print('Dennis Praet')
    print('Nationality:         ' + pra_nation)
    print('Appearances:         ' + pra_appearances)
    print('Goals:               ' + pra_goals)
    print('Passes:              ' + pra_passes)
    print('Passes on target:    ' + pra_passes_tar)
    print('Shots:               ' + pra_shots)
    print('Shots on target:     ' + pra_shots_tar)
    print('Assists:             ' + pra_assists)
def pra_discipline_stats():
    print('Offsides:            ' + pra_yellow_cards)
    print('Fouls:               ' + pra_fouls)
    print('Yellow cards:        ' + pra_yellow_cards)
    print('Red Cards:           ' + pra_red_cards)

#Forwards print defintions<-----------------------------------------------------------------
# Jamie Vardy print defintions<-------------------------------------------------------------
def var_key_stats():
    print('Jamie Vardy')
    print('Nationality:         ' + var_nation)
    print('Appearances:         ' + var_appearances)
    print('Goals:               ' + var_goals)
    print('Goals w/ left foot:  ' + var_left)
    print('Goals w/ right foot: ' + var_right)
    print('Goals from headers:  ' + var_headers)
    print('Goals from free-kick:' + var_fkick)
    print('Goals from penalties:' + var_pen)
    print('Shots:               ' + var_shots)
    print('Shots on target:     ' + var_shots_tar)
    print('Assists:             ' + var_assists)
def var_discipline_stats():
    print('Offsides:            ' + var_yellow_cards)
    print('Fouls:               ' + var_fouls)
    print('Yellow cards:        ' + var_yellow_cards)
    print('Red Cards:           ' + var_red_cards)

# Kelechi Iheanacho print defintions<-------------------------------------------------------------
def ihe_key_stats():
    print('Kelechi Iheanacho')
    print('Nationality:         ' + ihe_nation)
    print('Appearances:         ' + ihe_appearances)
    print('Goals:               ' + ihe_goals)
    print('Goals w/ left foot:  ' + ihe_left)
    print('Goals w/ right foot: ' + ihe_right)
    print('Goals from headers:  ' + ihe_headers)
    print('Goals from free-kick:' + ihe_fkick)
    print('Goals from penalties:' + ihe_pen)
    print('Shots:               ' + ihe_shots)
    print('Shots on target:     ' + ihe_shots_tar)
    print('Assists:             ' + ihe_assists)
def ihe_discipline_stats():
    print('Offsides:            ' + ihe_yellow_cards)
    print('Fouls:               ' + ihe_fouls)
    print('Yellow cards:        ' + ihe_yellow_cards)
    print('Red Cards:           ' + ihe_red_cards)

# Ayoze Perez print defintions<-------------------------------------------------------------
def per_key_stats():
    print('Ayoze Perez')
    print('Nationality:         ' + per_nation)
    print('Appearances:         ' + per_appearances)
    print('Goals:               ' + per_goals)
    print('Goals w/ left foot:  ' + per_left)
    print('Goals w/ right foot: ' + per_right)
    print('Goals from headers:  ' + per_headers)
    print('Goals from free-kick:' + per_fkick)
    print('Goals from penalties:' + per_pen)
    print('Shots:               ' + per_shots)
    print('Shots on target:     ' + per_shots_tar)
    print('Assists:             ' + per_assists)
def per_discipline_stats():
    print('Offsides:            ' + per_yellow_cards)
    print('Fouls:               ' + per_fouls)
    print('Yellow cards:        ' + per_yellow_cards)
    print('Red Cards:           ' + per_red_cards)

start_player_stats_query()
