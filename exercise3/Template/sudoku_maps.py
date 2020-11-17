import numpy as np

sudoku1 = np.array([(3,0,0,0),
                    (0,0,2,0),
                    (0,1,0,0),
                    (0,0,0,2)])#.transpose()

sudoku2 = np.array([(0,0,0,0),
                    (0,0,1,0),
                    (4,0,0,0),
                    (0,2,0,3)])

sudoku3 = np.array([(0,1,0,0),
                    (4,2,0,0),
                    (0,0,2,0),
                    (0,3,0,0)])

sudoku4 = np.array([(0,0,2,1),
                    (0,0,0,3),
                    (4,0,0,0),
                    (1,2,0,0)])

sudoku5 = np.array([(1,0,0,0),
                    (0,0,0,2),
                    (0,3,0,0),
                    (0,0,0,4)])


for map_name in tuple(map(lambda i: "sudoku%i"%i, range(1,6))):
    map = globals()[map_name]
    globals()[map_name] = [[map[i][j]
                            for j in range(len(map))]
                           for i in range(len(map[0]))]

