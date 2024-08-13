"""модуль является точкой входа в программу"""
from CGame import CGame

game = CGame()

while True:
    game.start()
    userinput = input("Новая игра (Y/N)? ")
    if userinput.lower() != 'y':
        break
