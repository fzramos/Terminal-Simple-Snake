import numpy as np
import board1

def user_move():
    move = input("turn snake up(u), down(d), left(l), right(r), or no change (n): ")
    return move

def update_direct(direct_change, direct):
    changes = {
        "northu": "north",
        "northd": "north",
        "northl": "west",
        "northr": "east",
        "eastu": "north", 
        "eastd": "south", 
        "eastl": "east",       
        "eastr": "east",
        "southu": "south",
        "southd": "south",
        "southl": "west",
        "southr": "east",
        "westu": "north",
        "westd": "south",
        "westl": "west",
        "westr": "west"
    }
    new_direct = direct
    #find a better way to say( if anythig  typed in besides u,d,l,r change nothing)
    if (direct_change != "") and (direct_change in "udlr"):
        new_direct = changes[direct + direct_change]

    return new_direct

def update_mat_snake(dimen, snake_pos):
    board_mat = np.zeros(dimen)
    for i in range(snake_pos.shape[0]):
        if i == 0:
            board_mat[snake_pos[i,0],snake_pos[i,1]] = 2
        else:
            board_mat[snake_pos[i,0],snake_pos[i,1]] = 1
    return(board_mat)

#this is the key for updating the snake position
def change_pos(dimen, direct, snake_pos):
    #needs more options for whne you go off board
    new_snake = snake_pos
    snake_head = np.array([snake_pos[0,0], snake_pos[0,1]])
    new_snake = np.delete(new_snake, -1, 0)
    #this insert changes new_snake into a nromal list for some reasons
    if direct=="north":
        snake_head[0,] -= 1
    elif direct=="east":
        snake_head[1,] += 1
    elif direct=="south":
        snake_head[0,] += 1
    else:
        snake_head[1,] -= 1
    #find a way to optimize this (probably for loop)
    if snake_head[0,]==-1:
        snake_head[0,]=dimen[0]-1
    elif snake_head[0,]==dimen[0]:
        snake_head[0,]=0
    if snake_head[1,]==-1:
        snake_head[1,]=dimen[1]-1
    elif snake_head[1,]==dimen[1]:
        snake_head[1,]=0

    new_snake = np.insert(new_snake,0 , snake_head, axis = 0)
    return(new_snake)

def movement(dimen, pos_mat, direct_change, direct, snake_pos):
    new_direct = update_direct(direct_change, direct)
    new_snake_pos = change_pos(dimen, new_direct, snake_pos)
    new_board_mat = update_mat_snake(dimen, new_snake_pos)
    return (new_board_mat, new_direct, new_snake_pos)

def print_board_stuff(move_data):
    print(move_data[0])
    print(board1.make_board(move_data[0]))
    print("the snake is currently going " + move_data[1])
    print("the snakes position is :")
    print(move_data[2])

def game(dimen=(5,5)):
    #defining initial values for variables
    #first value in list is snake head, last is snake end
    snake_pos = [0,2,0,1,0,0]
    snake_pos = np.array(snake_pos).reshape((3,2))

    board_mat = update_mat_snake(dimen, snake_pos)

    direct = "east"
    move_data = (board_mat, direct, snake_pos)

    #printing initial board
    print_board_stuff(move_data)   

    i=0
    while i<100:
        direct_change = user_move()
        move_data = movement(dimen, move_data[0], direct_change, move_data[1], move_data[2])
        print_board_stuff(move_data)
        i += 1

if __name__ == "__main__":
    game()
