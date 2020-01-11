import game
import player
# Possible colors are:
# black, blue, cyan, green, magenta, red, white, yellow
playerNames = 'Andy Betty Charlie Dani Envy Fairy'.split()
colors      = 'red blue green yellow magenta cyan'.split()
teams       = [int(team) for team in '1 1 2 2 1 2'.split()]
playerList  = [player.Player(*attrs,None) for attrs in list(zip(playerNames, colors, teams))]
# playersDict = {"Andy":["red",1],"Betty":["blue",1],"Charlie":["green",2],"Dani":["yellow",2],"Envy":["magenta",1],"Fairy":["cyan",2]}

game1 = game.Game(playerList)
