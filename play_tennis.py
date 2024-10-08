from player import Player
from game import Game

nadal = Player("Rafael Nadal")
djokovic = Player("Novak djokovic")
shreeya = Player("Shreeya CY")

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