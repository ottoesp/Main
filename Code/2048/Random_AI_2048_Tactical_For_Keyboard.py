from Logic_Random_AI_Tactical_For_Keyboard import *
from copy import deepcopy
from random import randint
import timeit
import time
import sys
import keyboard
sys.setrecursionlimit(1500)



class GameAI:
    def __init__(self):
        self.ticker = 0
        self.first = 0
        self.last_move = 0
        self.save_move = 0

    def run(self, board_):
        self.bo = board_
        return self.make_move_choice(self.bo.board)

    def game_finished(self, board):
        for row in board:
            for square in row:
                if square == "__":
                    return False

            for i in range(1, 3):
                if row[i] == row[i + 1] or row[i] == row[i - 1]:
                    return False

        r_board = self.bo.Rotate_Board_Clockwise(board)
        for row in r_board:
            for i in range(1, 3):
                if row[i] == row[i + 1] or row[i] == row[i - 1]:
                    return False

        return True

    def try_key_up(self, board):
        board1 = self.bo.Rotate_Board_Clockwise(board)
        score = 0
        values_tbu = []
        for row in range(4):
            for column in range(4):
                for i in range(column - 1, -1, -1):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:
                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1:
                                score += 2 ** (int(board1[row][i]) + 1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."

                            else:
                                score += 2 ** (int(board1[row][i]) + 1)
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

        board1 = self.bo.Rotate_Board_Counter_Clockwise(board1)
        # print("\n", "up")
        # for i in range(4):
        #     print(board[i], board1[i])

        if board1 == board:
            return False

        return score, len(values_tbu)

    def try_key_down(self, board):
        board1 = self.bo.Rotate_Board_Clockwise(board)
        values_tbu = []
        score = 0
        for row in range(4):
            for column in range(3, -1, -1):

                for i in range(column + 1, 4):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:
                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1:
                                score += 2 ** (int(board1[row][i]) + 1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."

                            else:
                                score += 2 ** (int(board1[row][i]) + 1)
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

        board1 = self.bo.Rotate_Board_Counter_Clockwise(board1)

        # print("\n", "down")
        # for i in range(4):
        #     print(board[i], board1[i])

        if board1 == board:
            return False

        return score, len(values_tbu)

    def try_key_left(self, board):
        board1 = deepcopy(board)
        values_tbu = []
        score = 0
        for row in range(4):
            for column in range(4):
                for i in range(column - 1, -1, -1):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:

                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1:
                                score += 2 ** (int(board1[row][i]) + 1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."

                            else:
                                score += 2 ** (int(board1[row][i]) + 1)
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

        # print("\n", "left")
        # for i in range(4):
        #     print(board[i], board1[i])

        if board1 == board:
            return False

        return score, len(values_tbu)

    def try_key_right(self, board):
        board1 = deepcopy(board)
        values_tbu = []
        score = 0
        for row in range(4):
            for column in range(3, -1, -1):

                for i in range(column + 1, 4):
                    if board1[row][column] != "__":

                        if board1[row][i] == board1[row][column]:
                            board1[row][column] = "__"
                            values_tbu.append((row, i))

                            if len(str(int(board1[row][i]))) == 1:
                                score += 2 ** (int(board1[row][i]) + 1)
                                board1[row][i] = " " + str(int(board1[row][i]) + 1) + "."
                                break

                            else:
                                score += 2 ** (int(board1[row][i]) + 1)
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

        # print("\n", "right")
        # for i in range(4):
        #     print(board[i], board1[i])

        if board1 == board:
            return False

        return score, len(values_tbu)

    def make_move_choice(self, board):
        if self.ticker == 1:
            self.first = deepcopy(self.bo.board)
            self.last_move = deepcopy(self.save_move)

        if not self.game_finished(board):
            r = []

            up = self.try_key_up(board)
            if up:
                r.append(up)

            right = self.try_key_right(board)
            if right:
                r.append(right)

            down = self.try_key_down(board)
            if down:
                r.append(down)

            left = self.try_key_left(board)
            if left:
                r.append(left)

            if len(r) > 0:
                rand = r[randint(0, len(r) - 1)]

            else:
                rand = r[0]

            if rand == up:
                self.save_move = "up"
                self.bo.Key_Up()

            elif rand == right:
                self.save_move = "right"
                self.bo.Key_Right()

            elif rand == left:
                self.save_move = "left"
                self.bo.Key_Left()

            elif rand == down:
                self.save_move = "down"
                self.bo.Key_Down()

            self.ticker += 1
            self.make_move_choice(self.bo.board)
        else:
            return self.bo.score, self.bo.board


score = 0


def AI_Driver_Code(board):

    bo = Board(board)
    ai = GameAI()
    ai.bo = bo
    if not ai.game_finished(board):
        high_score = 0
        high_f_board = ""
        for i in range(50):
            ai = GameAI()
            bo = Board(board)
            ai.run(bo)
            # print(ai.bo.score)
            # for row in ai.first:
            #     print(row)
            # print("hs", high_score)
            if ai.bo.score > high_score:
                high_score = ai.bo.score
                high_f_board = ai.first

        # print("-----------------------------")
        # print(high_score)
        print(high_f_board)

        if ai.last_move == "up":
            keyboard.press_and_release("up arrow")
        elif ai.last_move == "down":
            keyboard.press_and_release("down arrow")
        elif ai.last_move == "left":
            keyboard.press_and_release("left arrow")
        elif ai.last_move == "right":
            keyboard.press_and_release("right arrow")

        AI_Driver_Code(high_f_board)

    else:
        for row in board:
            print(row)


def Driver_Code_Driver():
    b = Board([
        ['__', '__', '__', '__'],
        ['__', '__', '__', '__'],
        ['__', '__', '__', ' 1'],
        [' 1', '__', '__', '__']
    ])

    bb = b.board
    AI_Driver_Code(bb)


time.sleep(10)
start_time = timeit.default_timer()
Driver_Code_Driver()
print(timeit.default_timer() - start_time)


















