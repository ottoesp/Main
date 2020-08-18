from copy import deepcopy, copy
from math import inf

final = []


def print_board(board):
    for row in board:
        print(row)


def create_kings(board):
    for i in range(8):
        if board[0][i] == "W":
            board[0][i] = "w"

    for i in range(8):
        if board[7][i] == "B":
            board[7][i] = "b"


def king_game_over(row, column, board, turn):
    if turn == "W":
        king_type = "w"
        opposite_king = "b"
        opposite_turn = "B"
    else:
        king_type = "B"
        opposite_king = "w"
        opposite_turn = "W"

    """Up and left"""
    if row - 1 >= 0 and column - 1 >= 0 and board[row - 1][column - 1] not in [king_type, turn]:
        if board[row - 1][column - 1] == " ":
            return False

        elif row - 2 >= 0 and column - 2 >= 0:  # Can't jump off side of board
            if row - 2 >= 0 and column - 2 >= 0 and board[row - 1][column - 1] in [opposite_king, opposite_turn] and \
                board[row - 2][column - 2] == " ":
                return False

    """Up and right"""
    if row - 1 >= 0 and column + 1 <= 7 and board[row - 1][column + 1] not in [king_type, turn]:
        if board[row - 1][column + 1] == " ":
            return False

        elif row - 2 >= 0 and column + 2 <= 7:  # Can't jump off side of board
            if row - 2 >= 0 and column + 2 <= 7 and board[row - 1][column + 1] in [opposite_king, opposite_turn] and \
                board[row - 2][column + 2] == " ":
                return False

    """Down and Left"""
    if row + 1 <= 7 and column - 1 >= 0 and board[row + 1][column - 1] not in [king_type, turn]:
        if board[row + 1][column - 1] == " ":
            return False

        elif row + 2 <= 7 and column - 2 >= 0:  # Can't jump off side of board
            if row + 2 <= 7 and column - 2 >= 0 and board[row + 1][column - 1] in [opposite_king, opposite_turn] and \
                board[row + 2][column - 2] == " ":
                return False

    """Up and right"""
    if row + 1 <= 7 and column + 1 <= 7 and board[row + 1][column + 1] not in [king_type, turn]:
        if board[row + 1][column + 1] == " ":
            return False

        elif row + 2 <= 7 and column + 2 <= 7:  # Can't jump off side of board
            if row + 2 <= 7 and column + 2 <= 7 and board[row + 1][column + 1] == [opposite_king, opposite_turn] and \
                board[row + 2][column + 2] == " ":
                return False

    return True


def draw(board, turn):
    w_king_count = []
    b_king_count = []
    for row in range(8):
        for column in range(8):
            if board[row][column] not in ["w", " ", "b"]:
                return False
            elif board[row][column] == "w":
                w_king_count.append((row, column))
            elif board[row][column] == "b":
                b_king_count.append((row, column))
            if len(w_king_count) > 1 or len(b_king_count) > 1:
                return False

    if len(b_king_count) == 1 and len(w_king_count) == 1:
        if turn == "W":
            row, column = w_king_count[0]
            if ((row - 2 >= 0 and column - 2 >= 0 and board[row - 2][column - 2] == " ") and board[row - 1][column - 1] == "b") or \
                ((row - 2 >= 0 and column + 2 <= 7 and board[row - 2][column + 2] == " ") and board[row - 1][column + 1] == "b") or \
                ((row + 2 <= 7 and column - 2 >= 0 and board[row + 1][column - 1] == " ") and board[row + 1][column - 1] == "b") or \
                ((row + 2 <= 7 and column + 2 <= 7 and board[row + 2][column + 2] == " ") and board[row + 1][column + 1] == "b"):
                return False
        elif turn == "B":
            row, column = w_king_count[0]
            if (row - 1 >= 0 and column - 1 >= 0 and board[row - 1][column - 1] == "w") or \
                (row - 1 >= 0 and column + 1 <= 7 and board[row - 1][column + 1] == "w") or \
                (row + 1 <= 7 and column - 1 >= 0 and board[row + 1][column - 1] == "w") or \
                (row + 1 <= 7 and column + 1 <= 7 and board[row + 1][column + 1] == "w"):
                return False

    return True


def game_over(board, turn):
    if draw(board, turn):
        return True
    if turn == "W":
        if not any("w" in r or "W" in r for r in board):
            return True
        for row in range(8):
            for column in range(8):
                if board[row][column] == "w":
                    return king_game_over(row, column, board, "W")

                if board[row][column] in ["w", "W"]:
                    """Up and left"""
                    if row - 1 >= 0 and column - 1 >= 0 and board[row - 1][column - 1] not in ["w", "W"]:
                        if board[row - 1][column - 1] == " ":
                            return False

                        elif row - 2 >= 0 and column - 2 >= 0:  # Can't jump off side of board
                            if row - 2 >= 0 and column - 2 >= 0 and board[row - 1][column - 1] in ["B", "b"] and \
                                board[row - 2][column - 2] == " ":
                                return False

                    """Up and right"""
                    if row - 1 >= 0 and column + 1 <= 7 and board[row - 1][column + 1] not in ["w", "W"]:
                        if board[row - 1][column + 1] == " ":
                            return False

                        elif row - 2 >= 0 and column + 2 <= 7:  # Can't jump off side of board
                            if row - 2 >= 0 and column + 2 <= 7 and board[row - 1][column + 1] in ["B", "b"] and \
                                board[row - 2][column + 2] == " ":
                                return False

    elif turn == "B":
        if not any("b" in r or "B" in r for r in board):
            return True

        for row in range(8):
            for column in range(8):
                if board[row][column] == "b":
                    return king_game_over(row, column, board, turn)

                if board[row][column] in ["B", "b"]:

                    """Down and Left"""
                    if row + 1 <= 7 and column - 1 >= 0 and board[row + 1][column - 1] not in ["B", "b"]:
                        if board[row + 1][column - 1] == " ":
                            return False

                        elif row + 2 <= 7 and column - 2 >= 0:  # Can't jump off side of board
                            if row + 2 <= 7 and column - 2 >= 0 and board[row + 1][column - 1] in ["W", "w"] and \
                                board[row + 2][column - 2] == " ":
                                return False

                    """Up and right"""
                    if row + 1 <= 7 and column + 1 <= 7 and board[row + 1][column + 1] not in ["B", "b"]:
                        if board[row + 1][column + 1] == " ":
                            return False

                        elif row + 2 <= 7 and column + 2 <= 7:  # Can't jump off side of board
                            if row + 2 <= 7 and column + 2 <= 7 and board[row + 1][column + 1] == ["W", "w"] and \
                                board[row + 2][column + 2] == " ":
                                return False

    return True


def chain_attack(row, column, board):
    """Finds all possible end moves after a chain of attacks (must make attack in chain if possible)"""
    children = []
    can_play = False
    if board[row][column] in ["W", "w"]:
        if row - 2 >= 0 and column - 2 >= 0 and board[row - 1][column - 1] in ["b", "B"] \
            and board[row - 2][column - 2] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row - 1][column - 1] = " "
            pos_move[row - 2][column - 2] = "W"
            children.append((pos_move, -2, -2))
            can_play = True

        if row - 2 >= 0 and column + 2 <= 7 and board[row - 1][column + 1] in ["b", "B"] \
            and board[row - 2][column + 2] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row - 1][column + 1] = " "
            pos_move[row - 2][column + 2] = "W"

            children.append((pos_move, -2, +2))
            can_play = True

    elif board[row][column] in ["b", "B"]:
        if row + 2 <= 7 and column - 2 >= 0 and board[row + 1][column - 1] in ["W", "w"] and \
            board[row + 2][column - 2] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row + 1][column - 1] = " "
            pos_move[row + 2][column - 2] = "B"
            children.append((pos_move, +2, -2))
            can_play = True

        if row + 2 <= 7 and column + 2 <= 7 and board[row + 1][column + 1] in ["W", "w"] and \
            board[row + 2][column + 2] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row + 1][column + 1] = " "
            pos_move[row + 2][column + 2] = "B"
            children.append((pos_move, +2, +2))
            can_play = True

    if not can_play:
        global final
        final.append(board)
        return False

    else:
        end_child = []
        for child in children:
            if child:
                temp = chain_attack(row + child[1], column + child[2], child[0])
                if temp:
                    for c in end_child:
                        end_child.append(c)

        return end_child

    #  Children should be three tuples only


def king_chain_attack(row, column, board):
    """Finds all possible end moves after a chain of attacks (must make attack in chain if possible)"""
    king_type = board[row][column]

    if king_type == "w":
        turn = "W"
        opposite_king = "b"
        opposite_turn = "B"
    else:
        turn = "B"
        opposite_king = "w"
        opposite_turn = "W"

    children = []
    can_play = False

    if row - 2 >= 0 and column - 2 >= 0 and board[row - 1][column - 1] in [opposite_king, opposite_turn] \
        and board[row - 2][column - 2] == " ":
        pos_move = deepcopy(board)
        pos_move[row][column] = " "
        pos_move[row - 1][column - 1] = " "
        pos_move[row - 2][column - 2] = king_type
        children.append((pos_move, -2, -2))
        can_play = True

    if row - 2 >= 0 and column + 2 <= 7 and board[row - 1][column + 1] in [opposite_king, opposite_turn] \
        and board[row - 2][column + 2] == " ":
        pos_move = deepcopy(board)
        pos_move[row][column] = " "
        pos_move[row - 1][column + 1] = " "
        pos_move[row - 2][column + 2] = king_type
        children.append((pos_move, -2, +2))
        can_play = True

    if row + 2 <= 7 and column - 2 >= 0 and board[row + 1][column - 1] in [opposite_king, opposite_turn] and \
        board[row + 2][column - 2] == " ":
        pos_move = deepcopy(board)
        pos_move[row][column] = " "
        pos_move[row + 1][column - 1] = " "
        pos_move[row + 2][column - 2] = king_type
        children.append((pos_move, +2, -2))
        can_play = True

    if row + 2 <= 7 and column + 2 <= 7 and board[row + 1][column + 1] in [opposite_king, opposite_turn] and \
        board[row + 2][column + 2] == " ":
        pos_move = deepcopy(board)
        pos_move[row][column] = " "
        pos_move[row + 1][column + 1] = " "
        pos_move[row + 2][column + 2] = king_type
        children.append((pos_move, +2, +2))
        can_play = True

    if not can_play:
        global final
        final.append(board)
        return False

    else:
        end_child = []
        for child in children:
            if child:
                temp = king_chain_attack(row + child[1], column + child[2], child[0])
                if temp:
                    for c in end_child:
                        end_child.append(c)
        return end_child

        #  Children should be three tuples only


def get_score(board):
    """Compares 2 boards to see how many pieces each side lost, if it is positive then black lost more and if negative
    then white lost more"""
    score = 0
    if game_over(board, "W"):
        return -inf
    elif game_over(board, "B"):
        return inf
    for row in board:
        for square in row:
            if square == "W":
                score += 1
            elif square == "w":
                score += 2
            elif square == "B":
                score -= 1
            elif square == "b":
                score -= 2
    return score


def king_move(row, column, turn, board):
    """Identifies all possible moves for a given piece"""
    possible_moves = []
    global final
    king_type = board[row][column]

    """Move up and to left"""
    if row - 1 >= 0 and column - 1 >= 0 and \
        board[row - 1][column - 1] not in [turn, king_type]:  # Turn can be made

        if board[row - 1][column - 1] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row - 1][column - 1] = king_type
            possible_moves.append(pos_move)

        elif column - 2 >= 0 and row - 2 >= 0:  # Can't jump off side of board

            final = []
            king_chain_attack(row, column, board)
            for bob in final:
                possible_moves.append(bob)

    """Move up and to right"""
    if row - 1 >= 0 and column + 1 <= 7 and \
        board[row - 1][column + 1] not in [turn, king_type]:  # Turn can be made

        if board[row - 1][column + 1] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row - 1][column + 1] = king_type
            possible_moves.append(pos_move)

        elif row - 2 >= 0 and column + 2 <= 7:  # Can't jump off side of board
            if board[row - 2][column + 2] == " ":  # Check if space behind enemy

                final = []
                king_chain_attack(row, column, board)
                for bob in final:
                    possible_moves.append(bob)

    """Move down and to left"""
    if row + 1 <= 7 and column - 1 >= 0 and \
        board[row + 1][column - 1] not in [turn, king_type]:  # Turn can be made

        if board[row + 1][column - 1] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row + 1][column - 1] = king_type
            possible_moves.append(pos_move)

        elif row + 2 <= 7 and column - 2 >= 0:  # Can't jump off side of board
            if board[row + 2][column - 2] == " ":  # Check if space behind enemy

                final = []
                king_chain_attack(row, column, board)
                for bob in final:
                    possible_moves.append(bob)

    """Move down and to right"""
    if row + 1 <= 7 and column + 1 <= 7 and \
        board[row + 1][column + 1] not in [turn, king_type]:  # Turn can be made

        if board[row + 1][column + 1] == " ":
            pos_move = deepcopy(board)
            pos_move[row][column] = " "
            pos_move[row + 1][column + 1] = king_type
            possible_moves.append(pos_move)

        elif row + 2 <= 0 and column + 2 <= 0:  # Can't jump off side of board

            final = []
            king_chain_attack(row, column, board)
            for bob in final:
                possible_moves.append(bob)
    return possible_moves


def identify_move(row, column, turn, board, score=0):
    """Identifies all possible moves for a given piece"""
    possible_moves = []
    global final

    if turn == "W":  # White to move

        if board[row][column] == "w":
            for move in king_move(row, column, turn, board):
                possible_moves.append(move)

        else:
            """Move up and to left"""
            if row - 1 >= 0 and column - 1 >= 0 and \
                board[row - 1][column - 1] != "W":  # Turn can be made

                if board[row - 1][column - 1] == " ":
                    pos_move = deepcopy(board)
                    pos_move[row][column] = " "
                    pos_move[row - 1][column - 1] = "W"
                    possible_moves.append(pos_move)

                elif column - 2 >= 0 and row - 2 >= 0:  # Can't jump off side of board
                    if board[row - 2][column - 2] == " ":
                        final = []
                        chain_attack(row, column, board)
                        for bob in final:
                            possible_moves.append(bob)

            """Move up and to right"""
            if row - 1 >= 0 and column + 1 <= 7 and \
                board[row - 1][column + 1] != "W":  # Turn can be made

                if board[row - 1][column + 1] == " ":
                    pos_move = deepcopy(board)
                    pos_move[row][column] = " "
                    pos_move[row - 1][column + 1] = "W"
                    possible_moves.append(pos_move)

                elif row - 2 >= 0 and column + 2 <= 7:  # Can't jump off side of board
                    if board[row - 2][column + 2] == " ":  # Check if space behind enemy

                        final = []
                        chain_attack(row, column, board)
                        for bob in final:
                            possible_moves.append(bob)

    if turn == "B":  # Black to move

        if board[row][column] == "b":
            for move in king_move(row, column, turn, board):
                possible_moves.append(move)

        else:
            """Move down and to left"""
            if row + 1 <= 7 and column - 1 >= 0 and \
                board[row + 1][column - 1] != "B":  # Turn can be made

                if board[row + 1][column - 1] == " ":
                    pos_move = deepcopy(board)
                    pos_move[row][column] = " "
                    pos_move[row + 1][column - 1] = "B"
                    possible_moves.append(pos_move)

                elif row + 2 <= 7 and column - 2 >= 0:  # Can't jump off side of board
                    if board[row + 2][column - 2] == " ":  # Check if space behind enemy

                        final = []
                        chain_attack(row, column, board)
                        for bob in final:
                            possible_moves.append(bob)

            """Move down and to right"""
            if row + 1 <= 7 and column + 1 <= 7 and \
                board[row + 1][column + 1] != "B":  # Turn can be made

                if board[row + 1][column + 1] == " ":
                    pos_move = deepcopy(board)
                    pos_move[row][column] = " "
                    pos_move[row + 1][column + 1] = "B"
                    possible_moves.append(pos_move)

                elif row + 2 <= 0 and column + 2 <= 0:  # Can't jump off side of board

                    final = []
                    chain_attack(row, column, board)
                    for bob in final:
                        possible_moves.append(bob)
    for possible_move in possible_moves:
        create_kings(possible_move)

    return possible_moves


def identify_children(board, turn):
    """Identifies all possible moves from the current board and returns them as a list of boards"""
    children = []
    for row in range(8):
        for column in range(8):
            if board[row][column] == turn or board[row][column] == turn.lower():
                a = identify_move(row, column, turn, board)
                children.append(a)

    flat_list = []
    for sublist in children:
        for item in sublist:
            if len(item) > 0:
                flat_list.append(item)

    return flat_list


# b = [
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", "w", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", "b", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "]
# ]
#
# print(draw(b, "W"))
#
# b = [
#     [" ", " ", "b", " ", " ", " ", " ", " "],
#     [" ", "w", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "]
# ]
#
# print(draw(b, "W"))
#
# b = [
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", "w", " ", " ", " ", " ", " ", " "],
#     [" ", " ", "b", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " ", " ", " ", " "]
# ]
#
# print(draw(b, "W"))

# chain_attack(5, 4, b)
