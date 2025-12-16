import math
import random

# ================== GLOBALS ================== #

board = [[' ' for _ in range(3)] for _ in range(3)]

HUMAN = None
AI = None


# ================== UTILITY FUNCTIONS ================== #

def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '


def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


# ================== MINIMAX + ALPHA BETA ================== #

def minimax(is_maximizing, alpha, beta):
    if check_winner(AI):
        return 1
    if check_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = HUMAN
                    score = minimax(True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score


# ================== AI MOVES ================== #

def ai_easy():
    moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    i, j = random.choice(moves)
    board[i][j] = AI


def ai_medium():
    if random.random() < 0.5:
        ai_easy()
    else:
        ai_hard()


def ai_hard():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = AI


# ================== GAME MODES ================== #

def human_vs_ai():
    global HUMAN, AI
    reset_board()

    # ----- Symbol Selection -----
    while True:
        symbol = input("Choose your symbol (X or O): ").upper()
        if symbol in ['X', 'O']:
            HUMAN = symbol
            AI = 'O' if HUMAN == 'X' else 'X'
            break
        print("Invalid choice!")

    # ----- Difficulty -----
    print("\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    diff = input("Enter choice: ")

    if diff == '1':
        ai_move = ai_easy
        level = "Easy"
    elif diff == '2':
        ai_move = ai_medium
        level = "Medium"
    else:
        ai_move = ai_hard
        level = "Hard"

    # ----- Who Starts -----
    print("\nWho starts?")
    print("1. Human")
    print("2. AI")

    while True:
        start = input("Enter choice: ")
        if start in ['1', '2']:
            break
        print("Invalid choice!")

    print(f"\nHuman vs AI | Difficulty: {level}")
    print(f"Human: {HUMAN} | AI: {AI}")

    if start == '2':
        ai_move()

    # ----- Game Loop -----
    while True:
        print_board()

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != ' ':
            print("Invalid move!")
            continue

        board[row][col] = HUMAN

        if check_winner(HUMAN):
            print_board()
            print("Human wins ")
            break

        if is_draw():
            print_board()
            print("Draw ")
            break

        ai_move()

        if check_winner(AI):
            print_board()
            print("AI wins ")
            break

        if is_draw():
            print_board()
            print("Draw ")
            break


def human_vs_human():
    global HUMAN, AI
    reset_board()
    HUMAN = 'X'
    AI = 'O'
    current_player = HUMAN

    print("\nHuman vs Human")
    print("Player X vs Player O")

    while True:
        print_board()
        print(f"Player {current_player}'s turn")

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != ' ':
            print("Invalid move!")
            continue

        board[row][col] = current_player

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins ")
            break

        if is_draw():
            print_board()
            print("Draw ")
            break

        current_player = AI if current_player == HUMAN else HUMAN


# ================== MAIN MENU ================== #

def main():
    print("TIC TAC TOE")
    print("1. Human vs AI")
    print("2. Human vs Human")

    choice = input("Choose mode: ")

    if choice == '1':
        human_vs_ai()
    elif choice == '2':
        human_vs_human()
    else:
        print("Invalid choice!")


main()



