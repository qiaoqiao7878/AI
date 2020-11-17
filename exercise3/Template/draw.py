from tkinter import *
import numpy as np

def draw(sudoku, sudoku_init=None):
    canvas_width = 400
    canvas_height = 400

    box=[]

    for i in range( 4 ):
        for j in range(4):
             box.append( (canvas_width * 0.25 * j,
                        canvas_height * 0.25 * i,
                        canvas_width * 0.25 * (j+1),
                        canvas_height * 0.25 * (i+1) ) )

    master = Tk()

    w = Canvas(master, 
               width=canvas_width, 
               height=canvas_height)
    w.pack()

    for i in range(16):
        w.create_rectangle(box[i][0],box[i][1],box[i][2],box[i][3])

    for i in range(4):
        for j in range(4):
            if sudoku[i][j]!=0:
                if sudoku_init is not None and sudoku_init[i][j]!=sudoku[i][j]:
                    w.create_text(50 + 100*j, 50 + 100*i, text =sudoku[i][j], font=("Purisa", 50), fill="blue")
                else:
                    w.create_text(50 + 100*j, 50 + 100*i, text =sudoku[i][j], font=("Purisa", 50), fill="orange")

    w.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, width=5)
    w.create_line(0, canvas_height/2, canvas_width, canvas_height/2, width=5) 

    master.attributes('-topmost', True)
#     master.attributes('-topmost', False)
    mainloop()
