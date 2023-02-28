from views.player import PlayerView


class PlayerController:

    def __init__(self):
        self.view = PlayerView()

    def display_menu_players(self):
        """Menu Joueurs"""
        choice = self.view.player_menu()
        if choice == "1":
            # Lister les joueurs
            self.view.print_player_list()
            self.menu_players()
        elif choice == "2":
            # Ajouter un joueur
            self.new_player()
            self.menu_players()
        elif choice == "3":
            # Supprimer un joueur
            self.delete_player()
        elif choice == "4":
            # Retour
            self.main_menu_choice()
        else:
            print("Saisie invalide, veuillez réessayer")
            self.menu_players()
