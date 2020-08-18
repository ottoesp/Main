from tkinter import *
from copy import deepcopy

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
                if board[row][column] == " ":
                    pass
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

mainloop()
