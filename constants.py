from enum import Enum

BOARD_SIZE = 3
E_PLAYER_TYPE = Enum(value = 'PLAYER_TYPE', names = ['CROSS', 'ZERO'])
E_GAME_STATUS = Enum(value ='GAME_STATUS', names = ['PLAYING', 'FINISHED'])
player_names = {E_PLAYER_TYPE.CROSS: 'крестики', E_PLAYER_TYPE.ZERO: 'нолики'}
marker_names = {E_PLAYER_TYPE.CROSS: 'крестик', E_PLAYER_TYPE.ZERO: 'нолик'}