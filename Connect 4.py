ROWS = 6
COLUMN = 7
class Stack:
    def __init__(self):
        self._list = []
    def __len__(self):
        return len(self._list)    
    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return
    def peek(self):
        return self._list[-1]

#initilize the board
def create_game_board():
    board = []
    for i in range (ROWS):
        board.append(['  ']*COLUMN)
    return board

#Initliaze Stack
def initStacks():
    stacks = [ Stack(), Stack(), Stack(), 
         Stack(), Stack(), Stack(), Stack() ]
    return stacks

#print board
def print_game_board(board):
    print('-----------------------------------------')
    for i in range(ROWS):
        print('| '+' |  '.join(board[i])+'|')
        print('-----------------------------------------')
    colmun = ('  1     2     3     4     5     6     7')
    print(colmun)

#Player Moves
def make_move(player,board,stacks):
    column = -1
    while column < 1 or column > COLUMN:
        try:
            column = int(input(f"{player}'s turn. Enter a column (1-7): "))
        except ValueError:
            print('Input must be integer between 1 and 7')
    
    if len(stacks[column-1]) == ROWS:
        print('Column full, try again...')
        return make_move(player, board, stacks)
    
    stacks[column-1].push(player)
    board[ROWS-len(stacks[column-1])][column-1] = player
    return board, stacks
    
#Check for wins
def check_wins(board,player):
    for i in range(ROWS):
        for j in range(COLUMN - 3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                return True
    for i in range(ROWS - 3):
        for j in range(COLUMN):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                return True
    for i in range(ROWS - 3):
        for j in range(COLUMN - 3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                return True
    for i in range(3, ROWS):
        for j in range(COLUMN - 3):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == player:
                return True
    return False

def main():
    board = create_game_board()
    stacks = initStacks()
    print_game_board(board)
    player = 'X'
    game = False
    while game == False:
        board,stacks = make_move(player,board,stacks)
        print_game_board(board)
        game = check_wins(board,player)
        if game:
            print(player + " Wins")
        else:
            player ='O' if player == 'X' else 'X'
if __name__ == '__main__':
    main()
