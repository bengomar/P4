class MainView:
    def display_main_menu(self):
        """Menu principal du programme"""
        print("*****************")
        print("* CENTRE ÉCHECS *")
        print("*****************")
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Lancer un tournoi ")
        print("   2.  Gestion des Joueurs ")
        print("   3.  Rapports ")
        print("   4.  Administration ")

        print("   5.  Sortir ")
        print("")

        option = input("Votre choix ---> ")
        choice = option
        return choice
