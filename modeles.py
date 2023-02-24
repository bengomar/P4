
class Tournament:
    def __init__(
<<<<<<< HEAD
        self,
        name: str,
        location: str,
        date_start: str,
        date_end: str,
        nb_round: str,
        description: str,
=======
        self, name: str, location: str, date_start: int, date_end: int, nb_round: int
>>>>>>> 14c7095bf60bf321b67ef64c8c9245b8d90bbeba
    ):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        self.description = description


class Player:
<<<<<<< HEAD
    def __init__(self, ident: str, surname: str, firstname: str, date_of_birth: str):
=======
    def __init__(
        self, ident: str, surname: str, firstname: str, date_of_birth: str
    ):
>>>>>>> 14c7095bf60bf321b67ef64c8c9245b8d90bbeba
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth

<<<<<<< HEAD

class Match:
    def __init__(self, player: str, opponent: str):
        self.player = player
        self.opponent = opponent
        self.match = ([player, 0], [opponent, 0])


class Round:
    matches = []

    def __init__(self, matches: list, rounds: int, name: str):
        self.matches = matches
        self.rounds = rounds
        self.name = "Round " + str(rounds)

    # def add_match(self, match: Match):
    #    pass
=======
class SearchPlayerIdent:
    def __init__(self, ident: str):
        self.ident = ident

class Rounds:
    def __init__(self, round_id, matchs):
        self.round_id = round_id
        self.matchs = matchs


class Matchs:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.players = [[player, 0], [opponent, 0]]
>>>>>>> 14c7095bf60bf321b67ef64c8c9245b8d90bbeba
