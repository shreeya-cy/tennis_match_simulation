from player import Player
from game import Game

nadal = Player("Rafael Nadal11")
djokovic = Player("Novak djokovic")

test_game = Game((nadal,djokovic),1)
print(test_game.scores)
test_game.add_score(nadal)
print(test_game.scores)

test_game.add_score(djokovic)
print(test_game.scores)


test_game.add_score(djokovic)
print(test_game.scores)

test_game.add_score(nadal)
print(test_game.scores)

test_game.add_score(nadal)
print(test_game.scores)

test_game.add_score(djokovic)
print(test_game.scores)

test_game.add_score(djokovic)
print(test_game.scores)

test_game.add_score(djokovic)
print(test_game.scores)

test_game.add_score(djokovic)
print(test_game.scores)