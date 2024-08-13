import re
from constants import E_GAME_STATUS
from constants import E_PLAYER_TYPE, player_names, marker_names, BOARD_SIZE
from CBoard import CBoard

"""Модуль непосредственно игры и ее состояния"""
class CGame:
    board = CBoard()
    current_player = None
    game_status = None
    winner = None
    step = 0

    def start(self):
        if self.game_status == E_GAME_STATUS.PLAYING:
            raise Exception('Ошибочная инициализация уже активной игры')

        print('===НАЧАЛО НОВОЙ ИГРЫ===')
        self.board.clear()
        self.current_player = E_PLAYER_TYPE.CROSS
        self.game_status = E_GAME_STATUS.PLAYING
        self.winner = None

        while self.game_status != E_GAME_STATUS.FINISHED:
            self.make_step()

        self.board.print()

        print('===ИГРА ЗАВЕРШЕНА===')
        if self.winner is None:
            print('Победитель не выявлен :-(')
        else:
            print(f'Победил игрок, использующий {player_names[self.winner]}')

    def make_step(self) -> None:
        self.step += 1
        print(f'[Раунд №{self.step}]')

        for i in range(2):
            self.board.print()
            self.get_user_input()
            self.winner = self.board.check_winning_state()

            if self.winner:
                self.game_status = E_GAME_STATUS.FINISHED
                break

            if self.board.is_completely_filled():
                self.game_status = E_GAME_STATUS.FINISHED
                break

            self.change_current_player()

    def get_user_input(self):
        print(f'Ход игрока, использующего {player_names[self.current_player]}')
        while True:
            user_input = input(
                f'> Укажите клетку, в которую будете ставить {marker_names[self.current_player]}, в виде пары чисел (номер строки и номер столбца), разделенных любыми символами: ')

            if not re.fullmatch(r'^\d+[^\d]+\d+$', user_input):
                print("Клетка указана некорректно. Повторите ввод.")
                continue

            matches = re.fullmatch(r'^(\d+)[^\d]+(\d+)$', user_input)
            row_index, column_index = int(matches.group(1)), int(matches.group(2))

            if row_index < 0 or row_index > BOARD_SIZE - 1:
                print(f'Некорректное значение строки. Укажите число в интервале [0, {BOARD_SIZE-1}]')
                continue

            if column_index < 0 or column_index > BOARD_SIZE - 1:
                print(f'Некорректное значение столбца. Укажите число в интервале [0, {BOARD_SIZE-1}]')
                continue

            if not self.board.is_empty_cell(row_index, column_index):
                print(f'Клетка {row_index, column_index} уже занята.')
                continue

            self.board.set_cell_value(row_index, column_index, self.current_player)
            break


    def change_current_player(self):
        self.current_player = E_PLAYER_TYPE.CROSS if self.current_player == E_PLAYER_TYPE.ZERO else E_PLAYER_TYPE.ZERO

    def get_current_player(self) -> E_PLAYER_TYPE:
        return self.current_player

    def get_status(self) -> E_GAME_STATUS:
        return self.game_status

    def get_winner(self) -> E_PLAYER_TYPE:
        return self.winner

    def get_step(self) -> int:
        return self.step
