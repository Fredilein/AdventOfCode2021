import sys
import pprint
import re
import numpy as np

with open('input.txt') as f:
    draws = f.readline().rstrip('\n').split(',')

    boards_inp = f.readlines()
    boards_inp = [b.rstrip() for b in boards_inp]

boards = []
for i in range(int(len(boards_inp) / 6)):
    board = np.empty((5, 5), int)
    for l in range(1, 6):
        board[l-1] = np.array(re.split('\s+', boards_inp[i*6+l].strip()))
    boards.append(board)

def calc_score(card, board):
    return np.sum((np.ones((5, 5)) - card) * board)

def has_won(card, board):
    winning = np.array([1, 1, 1, 1, 1])
    for i in range(5):
        if (card[i] == winning).all() or (card[:, i] == winning).all():
            return calc_score(card, board)
    return None

def num_moves(draws, board):
    filled = np.zeros((5, 5))
    moves = 1
    for d in draws:
        for l in range(len(board)):
            for c in range(len(board[l])):
                if board[l][c] == int(d):
                    filled[l][c] = 1
        winning_score = has_won(filled, board)
        if winning_score != None:
            return (moves, winning_score * int(d))
        moves += 1
    return (None, 0)

min_moves = 99999999
max_moves = 0
winning_score = None
losing_score = None
i = 1
for b in boards:
    (moves, score) = num_moves(draws, b)
    if moves == None:
        continue
    if moves < min_moves:
        min_moves = moves
        winning_score = score
    if moves > max_moves:
        max_moves = moves
        losing_score = score

print("Star 1: ", winning_score)
print("Star 2: ", losing_score)
