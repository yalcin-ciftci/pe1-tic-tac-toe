from random import randrange

# 1. Tahtayı ekrana yazdırır / Displays the current board
def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# 2. Boş karelerin koordinatlarını döner / Returns list of free squares as (row, col)
def make_list_of_free_fields(board):
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['O', 'X']:
                free.append((r, c))
    return free

# 3. Kullanıcıdan geçerli hamle alır / Takes a valid move from the player
def enter_move(board):
    while True:
        move = input("Enter your move: ")
        if move in "123456789" and len(move) == 1:
            move = int(move)
            row = (move - 1) // 3
            col = (move - 1) % 3
            if (row, col) in make_list_of_free_fields(board):
                board[row][col] = 'O'
                break

# 4. Kazananı kontrol eder / Checks if player or computer has won
def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

# 5. Bilgisayar rastgele boş kare seçer / Computer chooses a random free square
def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        pick = randrange(len(free))
        row, col = free[pick]
        board[row][col] = 'X'

# --- Oyun Başlangıcı / Game Start ---
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Tie!")
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Tie!")
        break