from Logic import *
from math import inf
from time import sleep
from operator import itemgetter
from tkinter import *
from copy import deepcopy
from random import  randint


root = Tk()


class Board():
    def __init__(self):
        self.tk_board_frames = [[], [], [], [], [], [], [], []]
        self.size_of_board = 800
        self.tk_board_main_frame = Frame(root, width=self.size_of_board, height=self.size_of_board)
        self.tk_board_labels = [[], [], [], [], [], [], [], []]
        self.bg_colour = "#ED6A5A"
        self.black_colour = "#435058"

    def display_board(self):
        for row in range(8):
            for column in range(8):

                if (row + column) % 2 == 0:
                    self.tk_board_frames[row].append(
                        Frame(self.tk_board_main_frame, height=self.size_of_board // 8,
                              width=self.size_of_board // 8, bg="White")
                    )

                else:
                    self.tk_board_frames[row].append(
                        Frame(self.tk_board_main_frame, height=self.size_of_board // 8,
                              width=self.size_of_board // 8, bg=self.bg_colour)
                    )

        for row in range(8):
            for column in range(8):
                self.tk_board_frames[row][column].grid(row=row, column=column)

        for row in range(8):
            for column in range(8):
                if (row + column) % 2 == 1:
                    self.tk_board_labels[row].append(
                        Label(self.tk_board_frames[row][column], text="⬤", font=("Times", 75, "bold"),
                              fg=self.bg_colour, bg=self.bg_colour)
                    )
                else:
                    self.tk_board_labels[row].append(None)

        for row in self.tk_board_labels:
            for label in row:
                if label is not None:
                    label.place(x=self.size_of_board / 8 / 2, y=self.size_of_board / 8 / 2 + 5, anchor=CENTER)

        self.tk_board_main_frame.grid(column=2, row=2)

    def update_board_data(self, board):
        for row in range(8):
            for column in range(8):
                if board[row][column] == " " and self.tk_board_labels[row][column] is not None:
                    self.tk_board_labels[row][column].config(text="⬤", fg=self.bg_colour)
                elif board[row][column] == "B":
                    self.tk_board_labels[row][column].config(text="◉", fg=self.black_colour)
                elif board[row][column] == "W":
                    self.tk_board_labels[row][column].config(text="◉", fg="White")

                elif board[row][column] == "b":
                    self.tk_board_labels[row][column].config(text="⊕", fg=self.black_colour)
                elif board[row][column] == "w":
                    self.tk_board_labels[row][column].config(text="⊕", fg="White")

    def move_piece(self, board):
        pass


def minimax(board, depth, alpha, beta, turn):
    global first_children

    if depth == 0 or game_over(board, turn):
        return get_score(board)

    if turn == "W":
        maxEval = -inf  # Worst possible max evaluation
        for child in identify_children(board, "W"):
            minimax_eval = minimax(child, depth - 1, alpha, beta, "B")
            if maxEval < minimax_eval:
                maxEval = minimax_eval
            if depth == 6:
                first_children.append((child, minimax_eval))
            alpha = max(alpha, minimax_eval)
            if beta <= alpha:
                break
        return maxEval

    if turn == "B":
        minEval = inf  # Worst possible max evaluation
        for child in identify_children(board, "B"):
            minimax_eval = minimax(child, depth - 1, alpha, beta, "W")
            if minEval > minimax_eval:
                minEval = minimax_eval
            if depth == 6:
                first_children.append((child, minimax_eval))
            beta = min(beta, minimax_eval)

            if beta <= alpha:
                break

        return minEval


first_children = []


def determine_best_child(board, turn):

    global first_children
    first_children = []
    mm = minimax(board, 6, -inf, inf, turn)
    print(first_children)
    if not game_over(board, turn):
        first_children.sort(key=itemgetter(1))

        best_children = []
        if turn == "W" and len(first_children) > 0:
            for child in first_children:
                print(child[1], "W")
                if child[1] == first_children[-1][1]:
                    best_children.append(child[0])
            rand = randint(0, len(best_children) - 1)
            print(first_children[-1][1])
            return best_children[rand]

        if turn == "B" and len(first_children) > 0:
            for child in first_children:
                print(child[1], "B")
                if child[1] == first_children[0][1]:
                    best_children.append(child[0])
            rand = randint(0, len(best_children) - 1)
            print(first_children[0][1])
            return best_children[rand]

    else:
        print("\n")
        print_board(board)
        return False


def play_game(board, turn):
    b = determine_best_child(board, turn)
    root.update()
    root.update_idletasks()
    global bo
    bo.update_board_data(board)

    if b:
        print_board(b)

        sleep(0)
        if turn == "B":
            root.title("Black to Move")
            play_game(b, "W")
        else:
            root.title("White to Move")
            play_game(b, "B")
    else:
        print(turn, "loses")


bo = Board()
bo.display_board()

root.update()
root.update_idletasks()

# bo.update_board_data([[' ', 'B', ' ', 'B', ' ', 'w', ' ', ' '],
#                         ['B', ' ', ' ', ' ', 'W', ' ', 'B', ' '],
#                         [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
#                         ['W', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
#                         [' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
#                         ['W', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
#                         [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
#                         ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ']])
play_game([
        [" ", "B", " ", "B", " ", "B", " ", "B"],
        ["B", " ", "B", " ", "B", " ", "B", " "],
        [" ", "B", " ", "B", " ", "B", " ", "B"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["W", " ", "W", " ", "W", " ", "W", " "],
        [" ", "W", " ", "W", " ", "W", " ", "W"],
        ["W", " ", "W", " ", "W", " ", "W", " "],
    ], "W")

root.update()
root.update_idletasks()
