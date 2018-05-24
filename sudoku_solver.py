from valid_sudoku import *
def compute_liberties(board):
    liberties = [[0 for i in range(9)] for k in range(9)]
    column = columns(board)
    subgrid = subgrids(board)
    min_liberty = [10,[-1,-1]]
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == ".":
                liberty = [str(j) for j in range(1,10)]
                for k in board[x]:
                    if k in liberty:
                        liberty.remove(k)
                for k in column[y]:
                    if k in liberty:
                        liberty.remove(k)
                subgrid_index  = 10
                if x < 3:
                    subgrid_index = y // 3 
                elif 2<x<6:
                    subgrid_index = y//3 +3
                elif  5<x<9:
                    subgrid_index = y//3 + 6
                for k in subgrid[subgrid_index]:
                    if k in liberty:
                        liberty.remove(k)
                liberties[x][y] = liberty
                if len(liberty) == 1:
                    return [[1,[x,y]],liberty]
                if len(liberty) < min_liberty[0]:
                    min_liberty = [len(liberty),[x,y]]
    return [min_liberty,liberties[min_liberty[1][0]][min_liberty[1][1]]]
            
def complete(board):
    for k in range(0,9):
        if "." in board[k]:
            return False
    return True

import copy
def sudoku_solver(board):
    s = Stack()
    s.push(board)
    flag = True
    
    while flag:
        current_board = s.pop()
        if valid_sudoku(current_board):
            if complete(current_board):
                return current_board
            target = compute_liberties(current_board)
            for k in target[1]:
                temporary_board = copy.deepcopy(current_board)
                temporary_board[target[0][1][0]][target[0][1][1]] = k
                s.push(temporary_board)
        if not s.nonempty():
            flag = False
    
    return False
        

class Stack:
    def __init__(self):
        self.head = None
    def push(self,value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if not self.head:
            return False
        return_value = self.head.val
        self.head = self.head.next
        return return_value
    def show(self):
        a = self.head
        while a:
            print(a.val)
            a = a.next
    def peek(self):
        return self.head.val
    def nonempty(self):
        return self.head != None
class ListNode:
    def __init__(self, x): 
        self.val = x
        self.next = None