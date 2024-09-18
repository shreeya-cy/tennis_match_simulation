from player import Player

class Game:
    def __init__(self, players = (Player(""), Player("")), game_number = 0):
        self.players = players
        self.game_number = game_number
        self.scores = {
            players[0]:0,
            players[1]:0
        }
        self.winner = None

    def __str__(self):
        score = self.scores.values()
        return f"{score[0]} - {score[1]}"

    def add_score(self, player):
        points = 0,15,30,40

        if(self.winner):
            return()

        if(self.scores[player] == 40):
            if('Ad' in self.scores.values()):
                for each in self.scores:
                    self.scores[each] = 40
            elif (list(self.scores.values()) == [40,40]):
                self.scores[player] = 'Ad'
            else:
                self.scores[player] = 'Game'
                self.winner = player
        elif(self.scores[player]=='Ad'):
            self.scores[player] = 'Game'
            self.winner = player
        else:
            self.scores[player] = points[points.index(self.scores[player]) + 1]
