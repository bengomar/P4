from modeles import Player, Tournament
from views.player import PlayerView
from views.tournament import TournamentView


class TournamentController:

    players = [
        Player(1, "CARLOS", "Roberto", "11112011"),
        Player(2, "MESSI", "Lionel", "11112011"),
        Player(3, "ZINEDINE", "Zidane", "11112011"),
        Player(4, "PETIT", "Emmanuel", "11112011"),
        Player(5, "DESCHAMPS", "Didier", "11112011"),
        Player(6, "VIEIRA", "Patrick", "11112011"),
        Player(7, "LIZARAZU", "Bixente", "11112011"),
        Player(8, "VIERA", "Patrick", "11112011")
    ]

    opponents_by_player = {}

    def __init__(self):
        self.tournament_view = TournamentView()


    def create_dico_player_playing(self, competitors):
        opponents_by_player = {}
        list_players_playing_1 = []

        for competitor in competitors:
            list_players_playing_1.append(competitor.ident)

        for player in list_players_playing_1:
            list_players_playing_2 = [i for i in list_players_playing_1 if i != player]
            opponents_by_player[player] = list_players_playing_2

        return opponents_by_player


    def start_tournament(self):

        # Display view to get inputs for the new tournament
        tournament_data = self.tournament_view.get_tournament_data()
        current_tournament = Tournament(*tournament_data)
        # current_tournament.save()

        # Display view to get players playing the tournament
        current_tournament.players = self.tournament_view.select_players_for_tournament(self.players)
        print(current_tournament.players)

        # Create dictionary to store who played with who
        opponents_by_player = self.create_dico_player_playing(current_tournament.players)

        # For round in rounds:
        for round_number in current_tournament.nb_round:
            pass
            # If round == 1:
                # pairs = generate_pairs_randomly(players)
            # else:
                # players = list_players_by_score
                # pairs = generate_pairs(players)

            # Create matches from pairs

            # For match in matches:

                # Enter results for match

        # Display all matches of all rounds in the tournament