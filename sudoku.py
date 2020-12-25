board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(b):
    find = find_empty(b)
    row, col = 0, 0
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(b, i, (row, col)):
            b[row][col] = i
            if solve(b):
                return True

            b[row][col] = 0
    return False

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - -")
        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(" {} ".format(b[i][j]), end="")
        print()

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                return (i, j)
    return None

def valid(b, num, pos):
    r, c = pos
    # checking row
    for i in range(len(b[0])):
        if b[r][i] == num and c != i:
            return False
    
    # checking column
    for i in range(len(b)):
        if b[i][c] == num and r != i:
            return False

    # check square
    x = r // 3
    y = c // 3
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if b[i][j] == num and i != r and j != c:
                return False
    
    return True

# print_board(board)
# solve_board(board)
# print()
# print()
# print()
# print_board(board)