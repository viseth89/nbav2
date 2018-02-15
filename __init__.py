from flask import Flask, render_template
from datetime import datetime
import nba_py

app = Flask(__name__)

@app.route('/')
def index():

    datetime_today = datetime.today()
    pretty_date_today = datetime_today.strftime('%b, %d, %Y')


    games=get_games(datetime_today)



    return render_template('index.html',title='Dialy Scores', games=games, pretty_date_today=pretty_date_today)

def get_games(date):
    scoreboard=nba_py.Scoreboard(month=date.month,day=date.day,
    year=date.year)

    line_score=scoreboard.line_score()
    games = []

    current_game = {}

    current_game_sequence = 0
    game_sequence_counter = 0

    for team in line_score:
        if (team['GAME_SEQUENCE'] != current_game_sequence):
            current_game['TEAM_1_ABBREVIATION'] = team['TEAM_ABBREVIATION']
            current_game['TEAM_1_WINS_LOSSES'] = team['TEAM_WINS_LOSSES']

            current_game['TEAM-1-PTS'] = team['PTS']
            current_game['TEAM-1-ID'] = team['TEAM_ID']

            current_game_sequence = team['GAME_SEQUENCE']
            game_sequence_counter += 1

        elif(game_sequence_counter == 1):
            current_game['TEAM_2_ABBREVIATION'] = team['TEAM_ABBREVIATION']
            current_game['TEAM_2_WINS_LOSSES'] = team['TEAM_WINS_LOSSES']

            current_game['TEAM-2-PTS'] = team['PTS']
            current_game['TEAM-2-ID'] = team['TEAM_ID']

            games.append(current_game)

            current_game = {}
            game_sequence_counter = 0

    return games


if __name__ == "__main__":
    # app.run(threaded=True)
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True )

    # line_score = scoreboard.line_score()

    # #list of games
    # games=[]
    # #Dictionary of the current game we are looking at
    # current_game = {}
    #
    # current_game_sequence = 0
    # game_sequence_counter = 0

    # line_score = scoreboard.line_score()
    #
    # #list of games
    # games = []
    # #dictionary of the current game we're looking at
    # current_game = {}
    #
    # current_game_sequence = 0
    #
    # game_sequence_counter = 0

    # for team in line_score:
    #     if (team['GAME_SEQUENCE'] != current_game_sequence):
    #         current_game['TEAM_1_ABBREVIATION'] = team['TEAM_ABBREVIATION']
    #         current_game['TEAM_1_WINS_LOSSES'] = team['TEAM_WINS_LOSSES']
    #
    #         current_game['TEAM_1_PTS'] = team['PTS']
    #         current_game['TEAM_1_ID'] = team['TEAM_ID']
    #
    #         current_game_sequene = team['GAME_SEQUENCE']
    #         game_sequence_counter += 1
    #     elif (game_sequence_counter == 1):
    #         current_game['TEAM_2_ABBREVIATION'] = team['TEAM_ABBREVIATION']
    #         current_game['TEAM_2_WINS_LOSSES'] = team['TEAM_WINS_LOSSES']
    #
    #         current_game['TEAM_2_PTS'] = team['PTS']
    #         current_game['TEAM_2_ID'] = team['TEAM_ID']
    #
    #         current_game['GAME_ID'] = team['GAME_ID']
    #
    #         games.append(current_game)
    #
    #         current_game = {}
    #         game_sequence_counter = 0
    #
    #     return games
