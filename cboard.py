"""Модуль работы с игровым полем"""
from constants import E_PLAYER_TYPE, BOARD_SIZE

"""Класс представления игрового поля"""
class CBoard:
    data = None

    def __init__(self):
        self.data = [
            ['-' for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)
        ]

    def clear(self):
        for row_idx in range(BOARD_SIZE):
            for column_idx in range(BOARD_SIZE):
                self.data[row_idx][column_idx] = '-'

    def print(self):
        print("Текущее состояние игрового поля")
        print(' ', ' '.join(map(str, list(range(BOARD_SIZE)))), ' ')
        for row_idx in range(BOARD_SIZE):
            print(row_idx, ' '.join(map(str, self.data[row_idx])), ' ')


    def set_cell_value(self, row_idx, column_id, player) -> int:
        self.data[row_idx][column_id] = 'x' if player == E_PLAYER_TYPE.CROSS else 'o'

    def get_cell_value(self, row_idx, column_idx) -> int:
        return self.data[row_idx][column_idx]

    def is_empty_cell(self, row_idx, column_idx):
        return self.data[row_idx][column_idx] == '-'

    def is_completely_filled(self):
        board_stringified = ''.join(str(cell) for row in self.data for cell in row)
        try:
            board_stringified.index('-')
            return False
        except ValueError:
            return True

    def check_winning_state(self):

        # проверим построчно наличие победителя
        for row in self.data:
            elems = list(set(row))
            if len(elems) == 1 and elems[0] != '-':
                return E_PLAYER_TYPE.CROSS if elems[0] == 'x' else E_PLAYER_TYPE.ZERO

        # проверим наличие победителя по столбцам
        for column_idx in range(BOARD_SIZE):
            elems = []

            for row_idx in range(BOARD_SIZE):
                elems.append(self.data[row_idx][column_idx])

            elems = list(set(elems))

            if len(elems) == 1 and elems[0] != '-':
                return E_PLAYER_TYPE.CROSS if elems[0] == 'x' else E_PLAYER_TYPE.ZERO

        # проверим наличие победителя на главной диагонали
        elems = []
        for row_idx in range(BOARD_SIZE):
            elems.append(self.data[row_idx][row_idx])

        elems = list(set(elems))

        if len(elems) == 1 and elems[0] != '-':
            return E_PLAYER_TYPE.CROSS if elems[0] == 'x' else E_PLAYER_TYPE.ZERO

        # проверим наличие победителя на побочной диагонали
        elems = []
        for row_idx in range(BOARD_SIZE):
            elems.append(self.data[row_idx][BOARD_SIZE - row_idx - 1])

        elems = list(set(elems))

        if len(elems) == 1 and elems[0] != '-':
            return E_PLAYER_TYPE.CROSS if elems[0] == 'x' else E_PLAYER_TYPE.ZERO

        return None
