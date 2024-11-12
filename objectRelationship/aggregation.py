class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

class Player:
    def __init__(self, name):
        self.name = name

team1 = Team('Liverpool')
player1=Player('andy')
team.add_player(player1)

print(team1.players)