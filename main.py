import random
import json
import datetime

#class score
#class player_name
#class date
"""
with open( "score_list.txt", "r") as score_file:
    score_list = json.loads( score_file.read() )
"""

class Result():
    def __init__(self, score, player_name, date):
        score.score=score
        score.player_name=player_name
        score.date=date

def game():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = 0

    print("Write your game name: ")
    player_name = input()

    for score_dict in score_list:
        print("Attempts made: {0}, Time of game: {1}, Player: {2}, Secret number: {3}, Wrong Guesses: {4}".format(score_dict["attempts"], score_dict["timestamp"], score_dict.get("Player"), score_dict.get("NumSecret"), score_dict["Failed"]))

    while True:
        guess = int(input( "Guess the secret number (1-30): " ))
        attempts += 1

        if guess == secret:
            print("You have guessed it!")
            print("Attempts needed: " + str( attempts ))

            score_data = {
                "Player": str(player_name),
                "timestamp": str(datetime.datetime.now()),
                "attempts": attempts,
                "NumSecret": secret,
                "Failed": wrong_guesses
            }
            score_list.append( score_data )

            with open( "score_list.txt", "w") as score_file:
                score_file.write( json.dumps( score_list ))
            break

        elif guess > secret:
            print("You guess is not correct, try smaller")
            wrong_guesses += 1
        else:
            print("Your guess is not correct, try bigger")
            wrong_guesses += 1

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list=json.loads(score_file.read())
        return score_list