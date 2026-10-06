board = [" " for _ in range(9)]

HUMAN = "X"
COMPUTER = "O"



def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("--+---+--")
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# Check whether the board is full
def is_full():
    return " " not in board



def utility():
    if check_winner(COMPUTER):
        return 1

    if check_winner(HUMAN):
        return -1

    return 0

def max_value():
    if check_winner(COMPUTER):
        return 1

    if check_winner(HUMAN):
        return -1

    if is_full():
        return 0

    value = -float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = COMPUTER

            value = max(value, min_value())

            board[i] = " "

    return value


def min_value():
    if check_winner(COMPUTER):
        return 1

    if check_winner(HUMAN):
        return -1

    if is_full():
        return 0

    value = float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = HUMAN

            value = min(value, max_value())

            board[i] = " "

    return value


def minimax_decision():
    best_value = -float("inf")
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = COMPUTER

            value = min_value()

            board[i] = " "

            if value > best_value:
                best_value = value
                best_move = i

    return best_move


print("TIC-TAC-TOE")
print("Human = X")
print("Computer = O")

display_board()

while True:

    
    row, col = map(
        int,
        input("Enter row and column: ").split()
    )

    position = (row - 1) * 3 + (col - 1)

    if position < 0 or position >= 9 or board[position] != " ":
        print("Invalid move. Try again.")
        continue

    board[position] = HUMAN
    display_board()

    if check_winner(HUMAN):
        print("Human Player Wins")
        break

    if is_full():
        print("Game Draw")
        break

    computer_move = minimax_decision()
    board[computer_move] = COMPUTER

    print("Computer's move:")
    display_board()

    
    if check_winner(COMPUTER):
        print("Computer Wins")
        break

    
    if is_full():
        print("Game Draw")
        break
