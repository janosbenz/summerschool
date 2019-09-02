# Exercise 1
# Take a string as an input
# Take a number as an input
# Return an n-element list of the string repeated n times
# E.g. multiline('*', 5)
#
def multiline(s,n):
    a_list = []
    for i in range(n): # Range function helps to iterate for loops for a number
        a_list.append(n * str(s))
    return a_list

print(multiline("LoL",5))

def multiline2(s,n):
    a_list = []
    aux = n
    while aux > 0:
        a_list.append(n * str(s))
        aux = aux - 1
    return a_list

print(multiline2("rAIn FOreSt ",6))

# Challenge

def triangle(s,n):
    a_list = []
    aux = 1
    while aux <= n:
        a_list.append(aux * str(s))
        aux = aux + 1
    return a_list

def printtriangle(triangle):
    for i in triangle:
        print(i)

printtriangle(triangle("*",5))

for i in range(1,10,2): # range function: range(start, end, steps)
    print(i)

def printline(a_list):
    print(", ".join(a_list))

printline(["Haha","sehr","lustig"])

def printline2(a_list):
    for i in a_list:
        print(i, end = ' ')

printline2(["Haha","sehr","lustig"])

def print_last_without(a_list):
    for i in range(len(a_list)): # zusätzliche index zahlen zur Liste
        if i < (len(a_list)-1): # len beginnt mit 1, Listen index beginnen mit 0
            print(a_list[i], end = ', ') # wenn index der Liste kleiner als 'Länge der Liste - 1' (=Index des letzten Elements)
        else:
            print(a_list[i], end = '.')

print_last_without(["Haha","sehr","lustig"])

some_matrix = [[1,2,3],[4,5,6],[7,8,9]]
def return_element(nested_list, row, column):
    print(nested_list[row][column])
return_element(some_matrix,2,1)

def change_element(nested_list, row, column, new_value):
    nested_list[row][column] = new_value
    return nested_list

def print_grid(nested_list):
    for a_list in nested_list:
        for element in a_list:
            print(element, end = ' ')
        print("\n")
    return True

some_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print_grid(change_element(some_matrix,1,1,"hello"))

######### Game of life ############
#" ".join() # Elemente einer Liste aneinander reihen, strings miteinander verknüpfen
# dead cells, alive cells als hilfsvariablen
# print grid
# globals() greift auf Variablen in global environment zu


#Basic setup
import random
alive = "●"
dead = "◯"

#function to make a random grid
def cellchoice():
    if random.choice([0,1]) == 1:
        return alive
    else:
        return dead

def make_grid(n):
    grid = []
    for i in range(n):
        line = []
        for i in range(n): # for loop für line muss innerhalb grid for loop sein, damit jede Linie in der Matrix eine neue ist
            line.append(cellchoice())
        grid.append(line)
    return(grid)

# printing the grid
def print_grid(a_grid):
    for line in a_grid:
        print(" ".join(line))

grid = make_grid(10)
print_grid(grid)

#function to look at the surrounding cells. Important condition: do not expect cells outside of the grid
def inspector(a_grid, line, column):
    col_range = [-1,0,1]
    local_matrix = ([None] * 3, [None] * 3, [None] * 3)
# Line 0
    if len(a_grid) >= line - 1 >= 0:
        aux= 0
        for i in col_range:
            if len(a_grid) >= column + i >= 0:
                local_matrix[0][aux] = a_grid[line - 1][column + i] #using an aux variable for the column of the local matrix; we need 0,1, and 2
            aux += 1
# Line 1
    aux = 0
    for i in col_range:
        if column + i >= 0:
            if len(a_grid) >= column + i:
                local_matrix[1][aux] = a_grid[line][column + i]
        aux += 1
# Line 2
    if len(a_grid) >= line + 1 >= 0:
        aux = 0
        for i in col_range:
            if len(a_grid) >= column + i >= 0:
                local_matrix[2][aux] = a_grid[line + 1][column + i]
            aux += 1
    mergematrix  = local_matrix[0]+local_matrix[1]+local_matrix[2]
    del mergematrix[4] # sollte center-cell löschen
    return mergematrix

print(inspector(grid,1,2))
# hood = inspector(grid,0,0)
# print(hood)

# count neighbours
def count_n(a_grid,line,column):
    found_neighbours = inspector(a_grid,line,column)
    neighbour_count = found_neighbours.count(alive)
    return neighbour_count
    # matrix_n = []
    # for row in range(len(a_grid)):
    #     for column in range(len(a_grid)):
    #         # currentState = a_grid[row][column]
    #         found_neighbours = inspector(a_grid,row,column)
    #         neighbour_count = found_neighbours.count(alive)
    #         # for neighbour in found_neighbours:
    #         #     if neighbour == alive:
    #         #         neighbour_count += 1
    #         matrix_n.append([row, column, neighbour_count])

                    # def c_neighbours(a_cell):
#     neighbours = 0
#     for i in a_hood: # cells around the cell
#             if element == alive:
#                 neighbours +=1
#     return neighbours
#
# def neighbours(a_grid):
#     neighbour_matrix = []
#     for line in range(len(a_grid)):
#         neighbour_line = []
#         for element in line:
#             neighbour_line.append(c_neighbours(inspector(a_grid, line, element)))
#     return neighbour_matrix


# predictor function
def is_alive(a_grid, line, column):
    neighbours = count_n(a_grid, line, column)
    if a_grid[line][column] == alive:
        if neighbours < 2:
            return False
        elif neighbours > 3: # why elif?
            return False
        else:
            return True
    elif a_grid[line][column] == dead:
        if neighbours == 3:
            return True
        else:
            return False

print(is_alive(grid, 1,1))

def next_grid(a_grid): #copied from Bryan
    size = len(a_grid)
    new_grid = []
    for row_index in range(0,size):
        new_row = []
        for col_index in range(0,size):
            if is_alive(a_grid,row_index,col_index) == True:
                new_row.append(alive)
            else:
                new_row.append(dead)
        new_grid.append(new_row)
    return new_grid

print(next_grid(grid))

# def predictor(old_grid):
#     killed = []
#     born = []
#     for line in range(old_grid):
#         for column in range(line):
#             neighbours = inspector(old_grid, line, column).count(alive) - 1
#             print(neighbours)
#             exit()
#             if old_grid[line][column] == alive:
#                 if neighbours < 2:
#                     killed.append([line, column])
#                 if neighbours > 3:
#                     killed.append([line, column])
#             else:
#                 if neighbours == 3:
#                     born.append([line, column])
#     return(killed)
#
# print(predictor(grid))

def play():
    pass
