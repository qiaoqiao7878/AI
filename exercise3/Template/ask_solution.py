from utils import expr
from field_var import field_var

def ask_solution(kb):
    sudoku_solution = [[0 for col in range(4)] for row in range(4)]
    # print(sudoku_ergebnis)
    for value in range(1,5):
        for x in range(0,4):
            for y in range(0,4): 
                result = kb.ask(expr(field_var(value, x, y)))
                if result: 
                    sudoku_solution[x][y] = value
                    
    return sudoku_solution