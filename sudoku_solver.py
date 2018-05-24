def compute_liberties(board):
    liberties = board
    column = columns(board)
    subgrid = subgrids(board)
    min_liberty = [10,[-1,-1]]
    for x in range(0,9):
        for y in range(0,9):
            liberty = set([str(x) for x in range(1,10)])
            for k in board[x]:
                if k in liberty:
                    liberty.remove(k)
            for k in column[y]:
                if k in liberty:
                    liberty.remove(k)
            subgrid_index  = 10
            if y < 3:
                subgrid_index = x // 3 
            elif 2<y<6:
                subgrid_index = x//3 +3
            elif  5<y<9:
                subgrid_index = x//3 + 6
            for k in subgrid[subgrid_index]:
                if k in liberty:
                    liberty.remove(k)
            liberties[x][y] = liberty
            if len(liberty) < min_liberty[0]:
                min_liberty = [len(liberty),[x,y]]
    return [min_liberty,liberties[x][y]]