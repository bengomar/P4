class ReportController:

    def menu_reports(self):
        """Menu Rapports"""
        choice = ReportsView().reports_infos_menu()

        if choice == "1":
            # Liste des joueurs par ordre alphabétique
            PlayerView().print_player_list()
            DatabasesTinydb().sorted_players_list_ident()
            Waiting.wait()
            self.menu_reports()
        elif choice == "2":
            # Liste des tournois
            DatabasesTinydb().tournaments_list_formated()
            Waiting.wait()
            self.menu_reports()
        elif choice == "3":
            # Données d'un tournoi
            print("nom et dates d’un tournoi donné")
            Waiting.wait()
            self.menu_reports()
        elif choice == "4":
            # Liste des joueurs du dernier tournoi par ordre alphabétique
            DatabasesTinydb().check_table_competitors()
            Waiting.wait()
            self.menu_reports()
        elif choice == "5":
            # Liste des tours et matchs du dernier tournoi
            print("Liste des tours et matchs du dernier tournoi")
            Waiting.wait()
            self.menu_reports()
        elif choice == "6":
            # Retour
            self.main_menu_choice()
        else:
            print("Saisie invalide, veuillez réessayer")
            Waiting.wait()
            self.menu_reports()