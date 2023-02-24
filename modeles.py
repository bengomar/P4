class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        date_start: str,
        date_end: str,
        nb_round: str,
        description: str,
    ):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        self.description = description


class Player:
    def __init__(self, ident: str, surname: str, firstname: str, date_of_birth: str):
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth


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
