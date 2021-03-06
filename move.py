import numpy as np
import board
import random

def user_move():
    move = input("turn snake up(w), down(s), left(a), right(d)"
        + ",or no change (n): ")
    return move

def update_direct(direct_change, direct):
    changes = {
        "northw": "north",
        "norths": "north",
        "northa": "west",
        "northd": "east",
        "eastw": "north", 
        "easts": "south", 
        "easta": "east",       
        "eastd": "east",
        "southw": "south",
        "souths": "south",
        "southa": "west",
        "southd": "east",
        "westw": "north",
        "wests": "south",
        "westa": "west",
        "westd": "west"
    }
    new_direct = direct
    if not direct_change and direct_change in "wasd":
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

def update_mat_full(dimen, snake_pos, apple_pos):
    board_mat = update_mat_snake(dimen, snake_pos)
    if board_mat[apple_pos[0], apple_pos[1]] == 0:
        board_mat[apple_pos[0], apple_pos[1]] = 3
    return(board_mat)

#this is the key for updating the snake position
def change_pos(dimen, direct, snake_pos, grow):
    #needs more options for whne you go off board
    new_snake = snake_pos
    snake_head = np.array([snake_pos[0,0], snake_pos[0,1]])
    if not grow:
        new_snake = np.delete(new_snake, -1, 0)
    grow = False
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
    return(new_snake, grow)

def apple_picker(dimen, new_snake_pos):
    board_mat = update_mat_snake(dimen, new_snake_pos)
    open_raw = np.where(board_mat == 0)
    open_pos = list(zip(open_raw[0], open_raw[1]))

    return random.choice(open_pos)

def snake_killer(dimen, new_snake_pos):
    board_mat = update_mat_snake(dimen, new_snake_pos)

    return np.where(board_mat == 2)[0].size == 0

def movement(dimen, pos_mat, direct_change, direct, snake_pos, apple_pos, grow):
    new_direct = update_direct(direct_change, direct)
    snake_grow = change_pos(dimen, new_direct, snake_pos, grow)
    new_snake_pos = snake_grow[0]
    new_grow = snake_grow[1]
    new_apple_pos = apple_pos
    
    #growth condition checker
    if (new_snake_pos[0, 0], new_snake_pos[0, 1]) == apple_pos:
        new_grow = True
        new_apple_pos = apple_picker(dimen, new_snake_pos)
    
    if snake_killer(dimen, new_snake_pos):
        #print("Game over")
        return "quit"
        
    new_board_mat = update_mat_full(dimen, new_snake_pos, new_apple_pos)
    return (new_board_mat, new_direct, new_snake_pos, new_apple_pos, new_grow)


def print_board_stuff(move_data):
    print(move_data[0])
    print(board2.make_board(move_data[0]))
    #print("the snake is currently going " + move_data[1])
    #print("the snakes position is :")
    #print(move_data[2])

def game(dimen=(5,5)):
    #defining initial values for variables
    #first value in list is snake head, last is snake end
    snake_pos = np.array([[0,2],[0,1],[0,0]])
    direct = "east"
    grow = False
    #problem apple cant start at (1,1) right now, fix later
    board_mat = update_mat_snake(dimen, snake_pos)
    apple_pos = apple_picker(dimen, snake_pos)

    #temp reseting data to add apple to initial board data
    #maybe its a waste to fully rebuild the board data each time
    board_mat = update_mat_full(dimen, snake_pos, apple_pos)

    #maybe make this a dictionary so you can easily understand in functions?
    move_data = (board_mat, direct, snake_pos, apple_pos, grow)

    print_board_stuff(move_data)   

    i=0
    while i<600:
        direct_change = user_move()
        move_data = movement(dimen, move_data[0], direct_change, move_data[1], 
            move_data[2], move_data[3], move_data[4])
        if move_data == "quit":
            break
        print_board_stuff(move_data)

        i += 1

    print("Thanks for playing")
if __name__ == "__main__":
    game()
