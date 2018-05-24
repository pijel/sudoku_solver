def valid_sudoku(board):
    
    for k in board:
        if not check(k):
            return False
    for k in columns(board):
        if not check(k):
            return False
    for k in subgrids(board):
        if not check(k):
            return False
    return True

def columns(board):
    return [[board[i][k] for i in range(9)] for k in range(9)]

def subgrids(board):
    subgrids = []
    for x in (0,3,6):
        for y in (0,3,6):
            subgrids.append([board[i][k] for i in range(x,x+3) for k in range(y,y+3)])
    return subgrids
            
            
def check(arr):
    seen = set([])
    arr = [x for x in arr if x != "."]
    for k in arr:
        if k in seen:
            return False
        seen.add(k)
    return True