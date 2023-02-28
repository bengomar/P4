from datetime import datetime
from typing import List

from modeles import Player


class TournamentView:
    def get_tournament_data(self):
        name = input("Saisir le nom du tournoi: ").capitalize()
        location = input("Saisir le lieu du tournoi: ").capitalize()
        date_start = datetime.today().strftime("%d%m%Y-%H%M")
        date_end = ""
        nb_round = 4
        description = ""

        return [name, location, date_start, date_end, nb_round, description]

    def get_score_match(self):
        print("")
        choice = input("Votre choix ---> ")
        return choice

    def select_players_for_tournament(self, players: List[Player]) -> List[Player]:

        players_not_selected = players
        selected_players = []

        add_player_ended = False
        while add_player_ended is False:

            print("Liste des joueurs disponibles:")
            for index, player in enumerate(players_not_selected):
                print(f"{index} - {player}")

            print("Liste des joueurs selectionnes:")
            for index, player in enumerate(selected_players):
                print(f"{index} - {player}")
            else:
                print("Aucun joueur selectionne")

            print("Ajoutez un joueur au tournoi avec par position dans la liste:")
            index = int(input())
            selected_players.append(players.pop(index))

            choice = input("Continuez y/n:")
            if choice is "n":
                add_player_ended = True

        return selected_players
