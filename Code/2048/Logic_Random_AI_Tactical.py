from random import sample, random, randint
from copy import deepcopy
import keyboard


def Get_Row_Column(index):
    row = index // 4
    column = index % 4
    return row, column


class Board:
    def __init__(self, board):
        self.score = 0
        self.board = board
        # self.Reset_Board()

    def Key_Up(self):
        # keyboard.press_and_release("up arrow")
        board1 = self.Rotate_Board_Clockwise(self.board)

        values_tbu = []
        for row in range(4):
            for column in range(4):
                for i in range(column - 1, -1, -1):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:
                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1 and int(board1[row][i]) != 9:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."

                            else:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = str(int(board1[row][i]) + 1) + "."
                            break

                        elif board1[row][i] != board1[row][column] and board1[row][i] != "__":
                            board1[row].insert(i + 1, board1[row].pop(column))
                            break

                        elif i == 0:
                            board1[row].insert(0, board1[row].pop(column))
                            break

        for update in values_tbu:
            row, column = update
            board1[row][column] = board1[row][column][0:2]

        board1 = self.Rotate_Board_Counter_Clockwise(board1)
        if board1 == self.board:
            self.board = board1
            return

        self.board = board1
        self.Generate_New()

    def Key_Down(self):
        # keyboard.press_and_release("down arrow")
        board1 = self.Rotate_Board_Clockwise(self.board)
        values_tbu = []
        for row in range(4):
            for column in range(3, -1, -1):

                for i in range(column + 1, 4):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:
                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1 and int(board1[row][i]) != 9:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."

                            else:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = str(int(board1[row][i]) + 1) + "."
                            break

                        elif board1[row][i] != board1[row][column] and board1[row][i] != "__":
                            board1[row].insert(i - 1, board1[row].pop(column))
                            break

                        elif i == 3:
                            board1[row].append(board1[row].pop(column))
                            break

        for update in values_tbu:
            row, column = update
            board1[row][column] = board1[row][column][0:2]

        board1 = self.Rotate_Board_Counter_Clockwise(board1)
        if board1 == self.board:
            self.board = board1
            return

        self.board = board1
        self.Generate_New()

    def Key_Left(self, major=False):
        # keyboard.press_and_release("left arrow")
        board1 = deepcopy(self.board)
        values_tbu = []
        for row in range(4):
            for column in range(4):
                for i in range(column - 1, -1, -1):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:

                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1 and int(board1[row][i]) != 9:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."

                            else:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = str(int(board1[row][i]) + 1) + "."
                            break

                        elif board1[row][i] != board1[row][column] and board1[row][i] != "__":
                            board1[row].insert(i + 1, board1[row].pop(column))
                            break

                        elif i == 0:
                            board1[row].insert(0, board1[row].pop(column))
                            break

        for update in values_tbu:
            row, column = update
            board1[row][column] = board1[row][column][0:2]

        if board1 == self.board:
            self.board = board1
            return

        self.board = board1
        self.Generate_New()

    def Key_Right(self):
        # keyboard.press_and_release("right arrow")
        board1 = deepcopy(self.board)
        values_tbu = []
        for row in range(4):
            for column in range(3, -1, -1):

                for i in range(column + 1, 4):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:
                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1 and int(board1[row][i]) != 9:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."
                                break

                            else:
                                self.score += 2**(int(board1[row][i])+1)
                                board1[row][i] = str(int(board1[row][i]) + 1) + "."
                                break

                        elif board1[row][i] != board1[row][column] and board1[row][i] != "__":
                            board1[row].insert(i - 1, board1[row].pop(column))
                            break

                        elif i == 3:
                            board1[row].append(board1[row].pop(column))
                            break

        for update in values_tbu:
            row, column = update
            board1[row][column] = board1[row][column][0:2]

        if board1 == self.board:
            self.board = board1
            return

        self.board = board1
        self.Generate_New()

    def Reset_Board(self):
        for row in range(4):
            for square in range(4):
                self.board[row][square] = '__'
        randoms = sample(range(16), k=2)
        for rand in randoms:
            if random() > 0.18:
                self.board[Get_Row_Column(rand)[0]][Get_Row_Column(rand)[1]] = ' 1'
            else:
                self.board[Get_Row_Column(rand)[0]][Get_Row_Column(rand)[1]] = ' 2'

    def Print_Board(self, board):
        for row in board:
            print(row)

    def Find_Empties(self):
        empties = []
        for row in range(4):
            for column in range(4):
                if self.board[row][column] == "__":
                    empties.append((row, column))
        return empties

    def Generate_New(self):
        row, column = self.Find_Empties()[randint(0, len(self.Find_Empties()) - 1)]
        if random() > 0.18:
            self.board[row][column] = ' 1'
        else:
            self.board[row][column] = ' 2'

    @staticmethod
    def Rotate_Board_Clockwise(board):
        rotated_board = [[], [], [], []]
        for row in range(4):
            for column in range(4):
                rotated_board[column].append(board[row][column])
        return rotated_board

    @staticmethod
    def Rotate_Board_Counter_Clockwise(board):
        rotated_board = [[], [], [], []]
        for row in range(4):
            for column in range(4):
                rotated_board[column].append(board[row][column])
        return rotated_board

# b = Board([
#             ['__', '__', '__', '__'],
#             ['__', '__', '__', '__'],
#             ['__', '__', '__', '__'],
#             ['__', '__', '__', '__']
#         ])
# b.Print_Board()
# print("\n")
# b.Key_Left()
# b.Print_Board()
