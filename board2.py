import numpy as np

def make_board(mat):
    visual = " _" * (mat.shape[1]) + "\n"
    board_el = {
        0:"|_",
        1:" +",
        2:" o",
        3:" x"
        #2 is the head of snake
        #x is the apple that makes snake longer
    }
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            visual += board_el[mat[i,j]]
        visual += "|\n"
    return(visual)


if __name__ == "__main__":
    board_size = (5,5)

    board_values = np.zeros(board_size)
    board_values [3, :] = 1
    board_values[0, 0] = 2
    snake_pos = [(0,0), (0,1), (0,2)]
    print(board_values)
    print(make_board(board_values))
    print(np.sum(board_values==1))