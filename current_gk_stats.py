import sys
sch_name = str('kasper schmeichel')
sch_initials = str('ks')

war_name = str('danny ward')
war_initials = str('dw')

jak_name = str('eldin jakupovic')
jak_initials = str('ej')

#Basic statistic values - strings used for concatenation
sch_saves = str(21) #Kasper Schmeichel<-----------------------------------------------------------
sch_punches = str(1)#basic_stats
sch_high_claims = str(5)
sch_catches = str(3)
sch_sweeps = str(3)
sch_throw_outs = str(38)
sch_goal_kicks = str(65)
sch_clean_sheets = str(2)
sch_goals_conceded = str(7)

sch_assists = str(0)#team_play
sch_passes_completed = str(167)
sch_passes_per_game = str(28)
sch_pass_accuracy = str(74)

sch_appearances = str(8)#performance_stats
sch_total_saves = str(21)
sch_saves_per_game = str(2.6)
sch_wins = str(4)
sch_draws = str(2)
sch_losses = str(2)

sch_yellow_cards = str(0)#discipline_stats
sch_red_cards = str(0)
sch_fouls = str(0)
#<-----------------------------------------------------------------------------------------


war_saves = str(0) #Danny Ward<-----------------------------------------------------------
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
#<-----------------------------------------------------------------------------------------

jak_saves = str(0) #Eldin Jakupovic<-----------------------------------------------------------
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
#<-----------------------------------------------------------------------------------------

def start_gk_player_stats(): #Code for the user query positioned on startup
    starter_user_query = input(
        "\nType the name or initials of the keeper:\nKasper Schmeichel (KS)\nDanny Ward (DW)\nEldin Jakupovic (EJ)\n").lower()
    if starter_user_query == sch_name or sch_initials:
        sch_basic_stats()
        sch_team_play()
        sch_performance_stats()
        sch_discipline_stats()
        sys.exit()
    if starter_user_query == war_name or war_initials:
        war_basic_stats()
        war_team_play()
        war_performance_stats()
        war_discipline_stats()
        sys.exit()
    if starter_user_query == jak_name or jak_initials:
        jak_basic_stats()
        jak_team_play()
        jak_performance_stats()
        jak_discipline_stats()
        sys.exit()
    else: start_gk_player_stats()

#Kasper Schmeichel print defintions<-------------------------------------------------------------
def sch_basic_stats():
        print("Saves:           " + sch_saves)
        print("Punches:         " + sch_punches)
        print("High Claims:     " + sch_high_claims)
        print("Catches:         " + sch_catches)
        print("Sweeps:          " + sch_sweeps)
        print("Throw Outs:      " + sch_throw_outs)
        print("Goal Kicks:      " + sch_goal_kicks)
        print("Clean Sheets:    " + sch_clean_sheets)
        print("Conceded:        " + sch_goals_conceded)
def sch_team_play():
        print("\nAssists:           " + sch_assists)
        print("Passes Completed:    " + sch_passes_completed)
        print("Passes Per Game:     " + sch_passes_per_game)
        print("Pass Accuracy:       " + sch_pass_accuracy + "%\n")
def sch_performance_stats():
        print("Appearances:     " + sch_appearances)
        print("Total Saves:     " + sch_total_saves)
        print("Saves Per Game:  " + sch_saves_per_game)
        print("Wins:            " + sch_wins)
        print("Draws:           " + sch_draws)
        print("Losses:          " + sch_losses)
def sch_discipline_stats():
        print("Fouls:           " + sch_fouls)
        print("Yellow Cards:    " + sch_yellow_cards)
        print("Red Cards:       " + sch_red_cards)

#Danny Ward print definition<-------------------------------------------------------------
def war_basic_stats():
        print("Saves:           " + war_saves)
        print("Punches:         " + war_punches)
        print("High Claims:     " + war_high_claims)
        print("Catches:         " + war_catches)
        print("Sweeps:          " + war_sweeps)
        print("Throw Outs:      " + war_throw_outs)
        print("Goal Kicks:      " + war_goal_kicks)
        print("Clean Sheets:    " + war_clean_sheets)
        print("Conceded:        " + war_goals_conceded)
def war_team_play():
        print("\nAssists:           " + war_assists)
        print("Passes Completed:    " + war_passes_completed)
        print("Passes Per Game:     " + war_passes_per_game)
        print("Pass Accuracy:       " + war_pass_accuracy + "%\n")
def war_performance_stats():
        print("Appearances:     " + war_appearances)
        print("Total Saves:     " + war_total_saves)
        print("Saves Per Game:  " + war_saves_per_game)
        print("Wins:            " + war_wins)
        print("Draws:           " + war_draws)
        print("Losses:          " + war_losses)
def war_discipline_stats():
        print("Fouls:           " + war_fouls)
        print("Yellow Cards:    " + war_yellow_cards)
        print("Red Cards:       " + war_red_cards)

#Eldin Jakupovic print definitions<-------------------------------------------------------------
def jak_basic_stats():
        print("Saves:           " + jak_saves)
        print("Punches:         " + jak_punches)
        print("High Claims:     " + jak_high_claims)
        print("Catches:         " + jak_catches)
        print("Sweeps:          " + jak_sweeps)
        print("Throw Outs:      " + jak_throw_outs)
        print("Goal Kicks:      " + jak_goal_kicks)
        print("Clean Sheets:    " + jak_clean_sheets)
        print("Conceded:        " + jak_goals_conceded)
def jak_team_play():
        print("\nAssists:           " + jak_assists)
        print("Passes Completed:    " + jak_passes_completed)
        print("Passes Per Game:     " + jak_passes_per_game)
        print("Pass Accuracy:       " + jak_pass_accuracy + "%\n")
def jak_performance_stats():
        print("Appearances:     " + jak_appearances)
        print("Total Saves:     " + jak_total_saves)
        print("Saves Per Game:  " + jak_saves_per_game)
        print("Wins:            " + jak_wins)
        print("Draws:           " + jak_draws)
        print("Losses:          " + jak_losses)
def jak_discipline_stats():
        print("Fouls:           " + jak_fouls)
        print("Yellow Cards:    " + jak_yellow_cards)
        print("Red Cards:       " + jak_red_cards)

start_gk_player_stats()
