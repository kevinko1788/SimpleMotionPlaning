# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # blocked coordinates
    blocked_list= []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] ==1:
                blocked_list.append([j,i])

    # action while 
    open_list=[]
    checked =[]
    path=[]
    current_position = []
    g_value = 0
    # initial starting point
    #open_list.append(init) do not since it is already checked
    checked.append(init)
    current_position = init
    path.append((g_value, init[0],init[1]))
    
    # action move delta current position + delta

    for move in delta:
        new_x = current_position[0] - move[0]
        new_y = current_position[1] - move[1]
        #check if out of boundary  
        if (new_x < 0) or (new_y <0) or (new_x > len(grid[0])) or (new_y > len(grid)):
            print('skipping')
            continue
        #check if it is in the blocked list    
        for b_coordinates in blocked_list:
            if [new_x,new_y] != b_coordinates:
                open_list.append([new_x,new_y])

    return path

print (search(grid,init,goal,cost))