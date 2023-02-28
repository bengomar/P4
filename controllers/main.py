from controllers.player import PlayerController
from controllers.report import ReportController
from controllers.tournament import TournamentController
from modeles import Player
from persistance import DatabasesTinydb
from views.main import MainView


class MainController:

    def __init__(self):
        self.view = MainView()
        self.database = DatabasesTinydb()

        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.report_controller = ReportController()

    def run(self):
        choice = self.view.display_main_menu()
        if choice == "1":
            self.tournament_controller.start_tournament()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print("Saisie invalide, veuillez réessayer")
            self.menu_admin()
