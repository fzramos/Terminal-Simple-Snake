import numpy as np

def make_board(mat):
    visual = " _" * (mat.shape[0]) + "\n"
    snake_bod = {
        0:"|_",
        1:" +",
        2:" o"
        #2 is the head of snake
    }
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            visual += snake_bod[mat[i,j]]
        visual += "|\n"
    return(visual)


if __name__ == "__main__":
    board_size = (5,5)

    board_values = np.zeros(board_size)
    board_values [3, :] = 1
    board_values[0, 0] = 2
    snake_pos = [(0,0), (0,1), (0,2)]
    #board_values[0, 0] = 3
    #board_values[0, 1] = 2
    #board_values[0, 2] = 1
    print(board_values)
    print(make_board(board_values))
    print(np.sum(board_values==1))