def print_board(board):
    for row in board:
        print(row)
    print()


def is_safe(board,row ,col , n):
    # column
    for i in range(row):
        if board[i][col] ==1:
            return False
        
    # Upper left diagonal 
    i , j = row -1 ,col -1
    while i >= 0 and j >= 0:
        if board[i][j]==1:
            return False
        i -=1
        j -=1

    # Upper right diagonal
    i , j = row -1 , col +1
    while i >= 0 and j < n:
        if board[i][j]==1:
            return False
        i -=1
        j +=1
    
    return True

def solve_n_queen(board,row,n):
    if row == n :
        print('All Queens Placed')
        print_board(board)
        return True
    
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            if solve_n_queen(board,row+1,n):
                return True
            board[row][col]=0

    return False

n = int(input('Enter the value of N - '))
board=[[0 for _ in range(n)]for _ in range(n)]

board[0][2]=1
print("First queen placed at [0][0]\n")

solve_n_queen(board,1,n)
