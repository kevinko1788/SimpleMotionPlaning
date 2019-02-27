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

# blocked coordinates
blocked_list= []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] ==1:
            blocked_list.append([j,i])

def check_surrounding(current_position, open_list, g_value):
    for move in delta:
        #1 and 2 since current position [g_value, x, y]
        new_x = current_position[1] - move[0]
        new_y = current_position[2] - move[1]
        # check if out of boundary
        # action move delta current position + delta
        if (new_x < 0) or (new_y <0) or (new_x > len(grid[0])) or (new_y > len(grid)):
            #print('skipping')
            continue
        else:
            #check if it is in the blocked list    
            if not [new_x,new_y] in blocked_list:
                #created open coordinates
                open_list.append([g_value,new_x,new_y])
    return open_list
def move(open_list,g_value):
    return 

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    open_list=[]
    checked =[]
    path=[]
    g_value = 0
    current_position=[]

    found  = False
    resign = False

    # initial starting point
    open_list.append([0,init[0],init[1]])
    current_position = [0,init[0],init[1]]

    x = init[0]
    y = init[1]   
    
    print('open_list',open_list)
    print('current_position',current_position)
    # test = [[5,1,0],[4,0,1],[8,4,5],[9,2,3]]
    # print("current_position", sorted(test))
    
    # action while  
    while found is False and resign is False:
        if len(open_list) == 0:
            print ('fail')
            resign = True
            ##### Search ended without sucess
        else:
            path.append((g_value, x,y))
            #checked
            # checked.append()
            #remove from open_list()
            # openlist.remove()
            g_value+=1
            open_list = check_surrounding(current_position,open_list,g_value)

            #move
            open_list = sorted(open_list)
            current_position = open_list[0]

    # return path
print (search(grid,init,goal,cost))








