import numpy as np
from field_var import field_var

###################################
###### Your Code


def generate_knowledge(sudoku):
    # TODO generate the Knowledge Base
    # you can assume the sudoku is always a 4x4 array. 
    # Feel free to add helper functions in this file if you need them
    # Do not change any other notebooks or files only this file will be evaluated in the end.
    # It is also the only file you need to submit
    # Do not import any additional module or packages
    kb = []
    # TODO fill kb with propositions
    #pass #delete this line once you complete the function
    
    sudoku_test = [[0 for col in range(4)] for row in range(4)]
    for x in range(0,4):
        for y in range(0,4): 
            sudoku_test[x][y] = [1,2,3,4]
   
    sudoku_test,kb = init(sudoku,sudoku_test,kb)
    
    while(True):
        sudoku_test,kb = checkrow(sudoku,sudoku_test,kb)
        sudoku_test,kb = checkcol(sudoku,sudoku_test,kb)
        sudoku_test,kb = checksquare(sudoku,sudoku_test,kb)
        sudoku,sudoku_test,kb = add (sudoku,sudoku_test,kb)
       
        if min(sudoku[0])!= 0 and min(sudoku[1])!= 0 and min(sudoku[2])!= 0 and min(sudoku[3])!= 0:
            break
            
    
    return kb


def init(sudoku,sudoku_test,kb):
    for x in range(0,4):
        for y in range(0,4): 
            if sudoku[x][y] > 0:
                sudoku_test[x][y] = [sudoku[x][y]]
                new_proposition = field_var(int(sudoku[x][y]) ,x, y)
                kb.append(new_proposition)
                
    return sudoku_test,kb


def checkrow(sudoku,sudoku_test,kb):
    for x in range(0,4):
        for y in range(0,4): 
            value = int(sudoku[x][y])
            if value > 0:
                for y_1 in range(0,4): 
                    if y != y_1:
                        if value in sudoku_test[x][y_1]:
                            sudoku_test[x][y_1].remove(value)
                        
    return sudoku_test,kb

def checkcol(sudoku,sudoku_test,kb):
    for y in range(0,4):
        for x in range(0,4): 
            value = int(sudoku[x][y])
            if value > 0:
                for x_1 in range(0,4): 
                    if x != x_1:
                        if value in sudoku_test[x_1][y]:
                            sudoku_test[x_1][y].remove(value)
                        
    return sudoku_test,kb

def checksquare(sudoku,sudoku_test,kb):
    for t1 in (0,2): 
        for t2 in (0,2): 
            value = int(sudoku[t1][t2])
            if value > 0:
                if value in sudoku_test[t1][t2+1]:
                    sudoku_test[t1][t2+1].remove(value)
                if value in sudoku_test[t1+1][t2]:
                    sudoku_test[t1+1][t2].remove(value)
                if value in sudoku_test[t1+1][t2+1]:
                    sudoku_test[t1+1][t2+1].remove(value)    
              
                
            value = int(sudoku[t1][1+t2])
            if value > 0:
                if value in sudoku_test[t1][t2]:
                    sudoku_test[t1][t2].remove(value)
                if value in sudoku_test[t1+1][t2]:
                    sudoku_test[t1+1][t2].remove(value)
                if value in sudoku_test[t1+1][t2+1]:
                    sudoku_test[t1+1][t2+1].remove(value)
               
            value = int(sudoku[1+t1][t2])
            if value > 0:
                if value in sudoku_test[t1][t2]:
                    sudoku_test[t1][t2].remove(value)
                if value in sudoku_test[t1][t2+1]:
                    sudoku_test[t1][t2+1].remove(value)
                if value in sudoku_test[t1+1][t2+1]:
                    sudoku_test[t1+1][t2+1].remove(value)
               
            value = int(sudoku[1+t1][1+t2])
            if value > 0:
                if value in sudoku_test[t1][t2]:
                    sudoku_test[t1][t2].remove(value)
                if value in sudoku_test[t1][t2+1]:
                    sudoku_test[t1][t2+1].remove(value)
                if value in sudoku_test[t1+1][t2]:
                    sudoku_test[t1+1][t2].remove(value)
    return sudoku_test,kb

def add(sudoku,sudoku_test,kb):
    for x in range(0,4):
        for y in range(0,4):
            if (len(sudoku_test[x][y]))==1:
                sudoku[x][y] = (sudoku_test[x][y])[0]
                new_proposition = field_var(int(sudoku[x][y]) ,x, y) 
                kb.append(new_proposition)
    return sudoku,sudoku_test,kb


###################################