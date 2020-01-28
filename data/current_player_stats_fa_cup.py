#v0.02
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

# GOALKEEPER<-------------------------------------------------------------------------------------------------------
# Stats on the Leicester City website are incomplete, having to look elsewhere - https://www.transfermarkt.com/leicester-city/leistungsdaten/verein/1003/plus/1?reldata=FAC%262019
# Kasper Schmeichel<-------------

sch_nation = str('Danish')
sch_appearances = str(0)  # performance_stats
sch_yellow_cards = str(0)  # discipline_stats
sch_red_cards = str(0)
sch_clean_sheets = str(0)

# Danny Ward<---------------
war_nation = str('Welsh')
war_appearances = str(2)  # performance_stats
war_yellow_cards = str(0)  # discipline_stats
war_red_cards = str(0)
war_clean_sheets = str(2)

# Eldin Jakupovic<--------------
jak_nation = str('Swiss')
jak_appearances = str(0)  # performance_stats
jak_yellow_cards = str(0)  # discipline_stats
jak_red_cards = str(0)
jak_clean_sheets = str(0)

# DEFENCE<---------------------------------------------------------------------------------------------------------------
# James Justin stats<------
jus_nation = str('English')
jus_appearances = str(2)  # appearances
jus_goals = str(0)  # goals
jus_assists = str(1)
jus_yellow_cards = str(0)
jus_red_cards = str(0)
jus_fouls = str(0)

# Ben Chilwell stats<--------
chi_nation = str('English')
chi_appearances = str(1)  # appearances
chi_goals = str(0)  # goals
chi_assists = str(1)
chi_yellow_cards = str(0)
chi_red_cards = str(0)

# Caglar Soyuncu stats<---------
soy_nation = str('Turkish')
soy_appearances = str(2)  # appearances
soy_goals = str(0)  # goals
soy_assists = str(0)
soy_yellow_cards = str(0)
soy_red_cards = str(0)

# Wes Morgan stats<----------
mor_nation = str('Jamaican')
mor_appearances = str(2)  # appearances
mor_goals = str(0)  # goals
mor_assists = str(0)
mor_yellow_cards = str(0)
mor_red_cards = str(0)

# Jonny Evans stats<---------
eva_nation = str('Northern Irish')
eva_appearances = str(0)  # appearances
eva_goals = str(0)  # goals
eva_assists = str(0)
eva_yellow_cards = str(0)
eva_red_cards = str(0)

# Filip Benkovic<---------
ben_nation = str('Croatian')
ben_appearances = str(1)  # appearances
ben_goals = str(0)  # goals
ben_assists = str(0)
ben_yellow_cards = str(0)
ben_red_cards = str(0)

# Daniel Amartey<----------
ama_nation = str('Ghanaian')
ama_appearances = str(0)  # appearances
ama_goals = str(0)  # goals
ama_assists = str(0)
ama_yellow_cards = str(0)
ama_red_cards = str(0)

# Ricardo Pereira<-----------
rper_nation = str('Portuguese')
rper_appearances = str(0)  # appearances
rper_goals = str(0)  # goals
rper_assists = str(0)
rper_yellow_cards = str(0)
rper_red_cards = str(0)

# Christian Fuchs<------------
fuc_nation = str('Austria')
fuc_appearances = str(2)  # appearances
fuc_goals = str(0)  # goals
fuc_assists = str(0)
fuc_yellow_cards = str(0)
fuc_red_cards = str(0)

# MIDFIELD<--------------------------------------------------------------------------------
# Demarai Gray
gra_nation = str('English')
gra_appearances = str(2)  # appearances
gra_goals = str(0)  # goals
gra_assists = str(0)  #
gra_yellow_cards = str(0)
gra_red_cards = str(0)

# Youri Tielemans
tie_nation = str('Belgian')
tie_appearances = str(0)  # appearances
tie_goals = str(0)  # goals
tie_assists = str(0)  #
tie_yellow_cards = str(0)
tie_red_cards = str(0)

# James Maddison
mad_nation = str('English')
mad_appearances = str(1)  # appearances
mad_goals = str(0)  # goals
mad_assists = str(0)  #
mad_yellow_cards = str(0)
mad_red_cards = str(0)

# Marc Albighton
alb_nation = str('English')
alb_appearances = str(2)  # appearances
alb_goals = str(0)  # goals
alb_assists = str(0)  #
alb_yellow_cards = str(0)
alb_red_cards = str(0)

# Harvey Barnes
bar_nation = str('English')
bar_appearances = str(1)  # appearances
bar_goals = str(1)  # goals
bar_assists = str(0)  #
bar_yellow_cards = str(0)
bar_red_cards = str(0)

# Hamza Choudhury
cho_nation = str('English')
cho_appearances = str(2)  # appearances
cho_goals = str(0)  # goals
cho_assists = str(0)  #
cho_yellow_cards = str(0)
cho_red_cards = str(0)

# Matty James
jam_nation = str('English')
jam_appearances = str(0)  # appearances
jam_goals = str(0)  # goals
jam_assists = str(0)  #
jam_yellow_cards = str(0)
jam_red_cards = str(0)

# Nampalys Mendy
men_nation = str('French')
men_appearances = str(1)  # appearances
men_goals = str(0)  # goals
men_assists = str(0)  #
men_yellow_cards = str(0)
men_red_cards = str(0)

# Wilfred Ndidi
ndi_nation = str('Nigerian')
ndi_appearances = str(1)  # appearances
ndi_goals = str(0)  # goals
ndi_assists = str(0)  #
ndi_yellow_cards = str(0)
ndi_red_cards = str(0)

# Dennis Praet
pra_nation = str('Belgian')
pra_appearances = str(2)  # appearances
pra_goals = str(0)  # goals
pra_assists = str(0)  #
pra_yellow_cards = str(0)
pra_red_cards = str(0)


# FORWARD<-------------------------------------------------------------------------------------------
# key stats
var_nation = str('English')
var_appearances = str(0)  # appearances
var_goals = str(0)  # goals
var_assists = str(0)  #
var_yellow_cards = str(0)
var_red_cards = str(0)

# key stats
ihe_nation = str('Nigerian')
ihe_appearances = str(1)  # appearances
ihe_goals = str(1)  # goals
ihe_assists = str(0)  #
ihe_yellow_cards = str(0)
ihe_red_cards = str(0)

# key stats
per_nation = str('Spanish')
per_appearances = str(1)  # appearances
per_goals = str(0)  # goals
per_assists = str(0)  #
per_yellow_cards = str(0)
per_red_cards = str(0)

# User query switch<-------------------------------------------------------------------------------
def start_player_stats_query():  # Code for the user query positioned on startup
    starter_user_query = input('\nType the name or initials of the player, or "squad" to see the team list '
                               'or "exit" to close\n[All player statistics are in relation to the Carabao Cup]\n').lower()
    if (starter_user_query == lcfc_squad):
        list_squad()
        start_player_stats_query()
    if (starter_user_query == shut_down):
        sys.exit()
    if (starter_user_query == sch_name) or (starter_user_query == sch_initials):  # Schmeichel
        sch_basic_stats()
        sch_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == war_name) or (starter_user_query == war_initials):  # Ward
        war_basic_stats()
        war_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == jak_name) or (starter_user_query == jak_initials):  # Jakupovic
        jak_basic_stats()
        jak_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == jus_name) or (starter_user_query == jus_initials):  # Justin
        jus_key_stats()
        jus_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == chi_name) or (starter_user_query == chi_initials):  # Chilwell
        chi_key_stats()
        chi_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == soy_name) or (starter_user_query == soy_initials):  # Soyuncu
        soy_key_stats()
        soy_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == mor_name) or (starter_user_query == mor_initials):  # Morgan
        mor_key_stats()
        mor_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == eva_name) or (starter_user_query == eva_initials):  # Evans
        eva_key_stats()
        eva_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ben_name) or (starter_user_query == ben_initials):  # Benkovic
        ben_key_stats()
        ben_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ama_name) or (starter_user_query == ama_initials):  # Amartey
        ama_key_stats()
        ama_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == rper_name) or (starter_user_query == rper_initials):  # Pereira
        rper_key_stats()
        rper_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == fuc_name) or (starter_user_query == fuc_initials):  # Fuchs
        fuc_key_stats()
        fuc_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == gra_name) or (starter_user_query == gra_initials):  # Gray
        gra_key_stats()
        gra_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == tie_name) or (starter_user_query == tie_initials):  # Tielemans
        tie_key_stats()
        tie_discipline_stats()
    if (starter_user_query == mad_name) or (starter_user_query == mad_initials):  # Maddison
        mad_key_stats()
        mad_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == alb_name) or (starter_user_query == alb_initials):  # Albrighton
        alb_key_stats()
        alb_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == bar_name) or (starter_user_query == bar_initials):  # Barnes
        bar_key_stats()
        bar_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == cho_name) or (starter_user_query == cho_initials):  # Choudhury
        cho_key_stats()
        cho_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == jam_name) or (starter_user_query == jam_initials):  # James
        jam_key_stats()
        jam_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == men_name) or (starter_user_query == men_initials):  # Mendy
        men_key_stats()
        men_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ndi_name) or (starter_user_query == ndi_initials):  # Ndidi
        ndi_key_stats()
        ndi_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == pra_name) or (starter_user_query == pra_initials):  # Praet
        pra_key_stats()
        pra_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == var_name) or (starter_user_query == var_initials):  # Vardy
        var_key_stats()
        var_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == ihe_name) or (starter_user_query == ihe_initials):  # Iheanacho
        ihe_key_stats()
        ihe_discipline_stats()
        start_player_stats_query()
    if (starter_user_query == per_name) or (starter_user_query == per_initials):  # Perez
        per_key_stats()
        per_discipline_stats()
        start_player_stats_query()
    else:
        player_syntax_fail()

def player_syntax_fail():
    print('\nUnknown player / initials, try again or use "squad" for a full list\n')
    start_player_stats_query()

# Squad print definition<------------------------------------------------------------------------
def list_squad():
    print('\nGoalkeepers:')
    print(
        sch_name + ' - ' + sch_initials + ' | ' + war_name + ' - ' + war_initials + ' | ' + jak_name + ' - ' + jak_initials)
    print('\nDefense:')
    print(
        jus_name + ' - ' + jus_initials + ' | ' + chi_name + ' - ' + chi_initials + ' | ' + soy_name + ' - ' + soy_initials)
    print(
        mor_name + ' - ' + mor_initials + ' | ' + eva_name + ' - ' + eva_initials + ' | ' + ben_name + ' - ' + ben_initials)
    print(
        ama_name + ' - ' + ama_initials + ' | ' + rper_name + ' - ' + rper_initials + ' | ' + fuc_name + ' - ' + fuc_initials)
    print('\nMidfield:')
    print(
        gra_name + ' - ' + gra_initials + ' | ' + tie_name + ' - ' + tie_initials + ' | ' + mad_name + ' - ' + mad_initials)
    print(
        alb_name + ' - ' + alb_initials + ' | ' + bar_name + ' - ' + bar_initials + ' | ' + cho_name + ' - ' + cho_initials)
    print(
        jam_name + ' - ' + jam_initials + ' | ' + men_name + ' - ' + men_initials + ' | ' + ndi_name + ' - ' + ndi_initials)
    print(pra_name + ' - ' + pra_initials)
    print('\nForwards')
    print(
        var_name + ' - ' + var_initials + ' | ' + ihe_name + ' - ' + ihe_initials + ' | ' + per_name + ' - ' + per_initials)

# Player print definitions
# data can be difficult to find for this competition
# Kasper Schmeichel print defintions<-------------------------------------------------------------
def sch_basic_stats():
    print('Kasper Schmeichel')
    print('Nationality:     ' + sch_nation)
    print('Appearances:     ' + sch_appearances)
    print('Clean Sheets:    ' + sch_clean_sheets)

def sch_discipline_stats():
    print('Yellow Cards:    ' + sch_yellow_cards)
    print('Red Cards:       ' + sch_red_cards)

# Danny Ward print definition<-------------------------------------------------------------
def war_basic_stats():
    print('Danny Ward')
    print('Nationality:     ' + war_nation)
    print('Appearances:     ' + war_appearances)
    print('Clean Sheets:    ' + war_clean_sheets)

def war_discipline_stats():
    print('Yellow Cards:    ' + war_yellow_cards)
    print('Red Cards:       ' + war_red_cards)


# Eldin Jakupovic print definitions<-------------------------------------------------------------
def jak_basic_stats():
    print('Eldin Jakupovic')
    print('Nationality:     ' + jak_nation)
    print('Appearances:     ' + jak_appearances)
    print('Clean Sheets:    ' + jak_clean_sheets)

def jak_discipline_stats():
    print('Yellow Cards:    ' + jak_yellow_cards)
    print('Red Cards:       ' + jak_red_cards)


# James Justin <-------------------------------------------------------
def jus_key_stats():
    print('James Justin')
    print('Nationality:         ' + jus_nation)
    print('Appearances:         ' + jus_appearances)
    print('Goals:               ' + jus_goals)
    print('Assists:             ' + jus_assists)

def jus_discipline_stats():
    print('Yellow cards:        ' + jus_yellow_cards)
    print('Red Cards:           ' + jus_red_cards)


# Ben Chilwell <-------------------------------------------------------
def chi_key_stats():
    print('Ben Chilwell')
    print('Nationality:         ' + chi_nation)
    print('Appearances:         ' + chi_appearances)
    print('Goals:               ' + chi_goals)
    print('Assists:             ' + chi_assists)

def chi_discipline_stats():
    print('Yellow cards:        ' + chi_yellow_cards)
    print('Red Cards:           ' + chi_red_cards)


# Caglar Soyuncu stats<------------------------------------------------
def soy_key_stats():
    print('Caglar Soyuncu')
    print('Nationality:         ' + soy_nation)
    print('Appearances:         ' + soy_appearances)
    print('Goals:               ' + soy_goals)
    print('Assists:             ' + soy_assists)

def soy_discipline_stats():
    print('Yellow cards:        ' + soy_yellow_cards)
    print('Red Cards:           ' + soy_red_cards)


# Wes Morgan stats<------------------------------------------------------
def mor_key_stats():
    print('Wes Morgan')
    print('Nationality:         ' + mor_nation)
    print('Appearances:         ' + mor_appearances)
    print('Goals:               ' + mor_goals)
    print('Assists:             ' + mor_assists)

def mor_discipline_stats():
    print('Yellow cards:        ' + mor_yellow_cards)
    print('Red Cards:           ' + mor_red_cards)


# Jonny Evans stats<-------------------------------------------------------
def eva_key_stats():
    print('Jonny Evans')
    print('Nationality:         ' + eva_nation)
    print('Appearances:         ' + eva_appearances)
    print('Goals:               ' + eva_goals)
    print('Assists:             ' + eva_assists)

def eva_discipline_stats():
    print('Yellow cards:        ' + eva_yellow_cards)
    print('Red Cards:           ' + eva_red_cards)


# Filip Benkovic<--------------------------------------------------------
def ben_key_stats():
    print('Filip Benkovic')
    print('Nationality:         ' + ben_nation)
    print('Appearances:         ' + ben_appearances)
    print('Goals:               ' + ben_goals)
    print('Assists:             ' + ben_assists)

def ben_discipline_stats():
    print('Yellow cards:        ' + ben_yellow_cards)
    print('Red Cards:           ' + ben_red_cards)


# Daniel Amartey<----------------------------------------------------------
def ama_key_stats():
    print('Daniel Amartey')
    print('Nationality:         ' + ama_nation)
    print('Appearances:         ' + ama_appearances)
    print('Goals:               ' + ama_goals)
    print('Assists:             ' + ama_assists)

def ama_discipline_stats():
    print('Yellow cards:        ' + ama_yellow_cards)
    print('Red Cards:           ' + ama_red_cards)


# Ricardo Pereira<--------------------------------------------------------
def rper_key_stats():
    print('Ricardo Pereira')
    print('Nationality:         ' + rper_nation)
    print('Appearances:         ' + rper_appearances)
    print('Goals:               ' + rper_goals)
    print('Assists:             ' + rper_assists)

def rper_discipline_stats():
    print('Offsides:            ' + rper_yellow_cards)
    print('Red Cards:           ' + rper_red_cards)


# Christian Fuchs<----------------------------------------------------------
def fuc_key_stats():
    print('Christian Fuchs')
    print('Nationality:         ' + fuc_nation)
    print('Appearances:         ' + fuc_appearances)
    print('Goals:               ' + fuc_goals)
    print('Assists:             ' + fuc_assists)

def fuc_discipline_stats():
    print('Yellow cards:        ' + fuc_yellow_cards)
    print('Red Cards:           ' + fuc_red_cards)


# Midfield Print definitions<-------------------------------------------------------------------------------
# Demarai Gray print defintions<-------------------------------------------------------------
def gra_key_stats():
    print('Demarai Gray')
    print('Nationality:         ' + gra_nation)
    print('Appearances:         ' + gra_appearances)
    print('Goals:               ' + gra_goals)
    print('Assists:             ' + gra_assists)

def gra_discipline_stats():
    print('Yellow cards:        ' + gra_yellow_cards)
    print('Red Cards:           ' + gra_red_cards)


# Youri Tielemans print defintions<-------------------------------------------------------------
def tie_key_stats():
    print('Youri Tielemans')
    print('Nationality:         ' + tie_nation)
    print('Appearances:         ' + tie_appearances)
    print('Goals:               ' + tie_goals)
    print('Assists:             ' + tie_assists)

def tie_discipline_stats():
    print('Yellow cards:        ' + tie_yellow_cards)
    print('Red Cards:           ' + tie_red_cards)


# James Maddison print defintions<-------------------------------------------------------------
def mad_key_stats():
    print('James Maddison')
    print('Nationality:         ' + mad_nation)
    print('Appearances:         ' + mad_appearances)
    print('Goals:               ' + mad_goals)
    print('Assists:             ' + mad_assists)

def mad_discipline_stats():
    print('Yellow cards:        ' + mad_yellow_cards)
    print('Red Cards:           ' + mad_red_cards)


# Marc Albrighton print defintions<-------------------------------------------------------------
def alb_key_stats():
    print('Marc Albrighton')
    print('Nationality:         ' + alb_nation)
    print('Appearances:         ' + alb_appearances)
    print('Goals:               ' + alb_goals)
    print('Assists:             ' + alb_assists)

def alb_discipline_stats():
    print('Yellow cards:        ' + alb_yellow_cards)
    print('Red Cards:           ' + alb_red_cards)


# Harvey Barnes print defintions<-------------------------------------------------------------
def bar_key_stats():
    print('Harvey Barnes')
    print('Nationality:         ' + bar_nation)
    print('Appearances:         ' + bar_appearances)
    print('Goals:               ' + bar_goals)
    print('Assists:             ' + bar_assists)

def bar_discipline_stats():
    print('Yellow cards:        ' + bar_yellow_cards)
    print('Red Cards:           ' + bar_red_cards)


# Hamza Choudhury print defintions<-------------------------------------------------------------
def cho_key_stats():
    print('Hamza Choudhury')
    print('Nationality:         ' + cho_nation)
    print('Appearances:         ' + cho_appearances)
    print('Goals:               ' + cho_goals)
    print('Assists:             ' + cho_assists)

def cho_discipline_stats():
    print('Yellow cards:        ' + cho_yellow_cards)
    print('Red Cards:           ' + cho_red_cards)


# Matty James print defintions<-------------------------------------------------------------
def jam_key_stats():
    print('Matty James')
    print('Nationality:         ' + jam_nation)
    print('Appearances:         ' + jam_appearances)
    print('Goals:               ' + jam_goals)
    print('Assists:             ' + jam_assists)

def jam_discipline_stats():
    print('Yellow cards:        ' + jam_yellow_cards)
    print('Red Cards:           ' + jam_red_cards)


# Nampalys Mendy print defintions<-------------------------------------------------------------
def men_key_stats():
    print('Nampalys Mendy')
    print('Nationality:         ' + men_nation)
    print('Appearances:         ' + men_appearances)
    print('Goals:               ' + men_goals)
    print('Assists:             ' + men_assists)

def men_discipline_stats():
    print('Yellow cards:        ' + men_yellow_cards)
    print('Red Cards:           ' + men_red_cards)


# Wilfred Ndidi print defintions<-------------------------------------------------------------
def ndi_key_stats():
    print('Wilfred Ndidi')
    print('Nationality:         ' + ndi_nation)
    print('Appearances:         ' + ndi_appearances)
    print('Goals:               ' + ndi_goals)
    print('Assists:             ' + ndi_assists)

def ndi_discipline_stats():
    print('Yellow cards:        ' + ndi_yellow_cards)
    print('Red Cards:           ' + ndi_red_cards)


# Dennis Praet print defintions<-------------------------------------------------------------
def pra_key_stats():
    print('Dennis Praet')
    print('Nationality:         ' + pra_nation)
    print('Appearances:         ' + pra_appearances)
    print('Goals:               ' + pra_goals)
    print('Assists:             ' + pra_assists)

def pra_discipline_stats():
    print('Yellow cards:        ' + pra_yellow_cards)
    print('Red Cards:           ' + pra_red_cards)


# Forwards print defintions<-----------------------------------------------------------------
# Jamie Vardy print defintions<-------------------------------------------------------------
def var_key_stats():
    print('Jamie Vardy')
    print('Nationality:         ' + var_nation)
    print('Appearances:         ' + var_appearances)
    print('Goals:               ' + var_goals)
    print('Assists:             ' + var_assists)

def var_discipline_stats():
    print('Yellow cards:        ' + var_yellow_cards)
    print('Red Cards:           ' + var_red_cards)


# Kelechi Iheanacho print defintions<-------------------------------------------------------------
def ihe_key_stats():
    print('Kelechi Iheanacho')
    print('Nationality:         ' + ihe_nation)
    print('Appearances:         ' + ihe_appearances)
    print('Goals:               ' + ihe_goals)
    print('Assists:             ' + ihe_assists)

def ihe_discipline_stats():
    print('Yellow cards:        ' + ihe_yellow_cards)
    print('Red Cards:           ' + ihe_red_cards)


# Ayoze Perez print defintions<-------------------------------------------------------------
def per_key_stats():
    print('Ayoze Perez')
    print('Nationality:         ' + per_nation)
    print('Appearances:         ' + per_appearances)
    print('Goals:               ' + per_goals)
    print('Assists:             ' + per_assists)

def per_discipline_stats():
    print('Yellow cards:        ' + per_yellow_cards)
    print('Red Cards:           ' + per_red_cards)


start_player_stats_query()
