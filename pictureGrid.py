import time

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

tempx = []
for i in range(len(grid)):
    tempx.append(0)
returnarray = [] 
for i in range (len(grid[0])):
    for j in range (len(grid)):
        tempx[j] = grid[j][i]
    returnarray.append(tempx)
    print(returnarray[i])
    