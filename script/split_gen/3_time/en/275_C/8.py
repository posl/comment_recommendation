def main():
    #get input
    board = []
    for i in range(9):
        board.append(input())
    #find all squares
    squares = []
    for i in range(8):
        for j in range(8):
            squares.append([(i+1,j+1),(i+1,j+2),(i+2,j+2),(i+2,j+1)])
    #count squares
    count = 0
    for square in squares:
        if board[square[0][0]-1][square[0][1]-1] == "#" and board[square[1][0]-1][square[1][1]-1] == "#" and board[square[2][0]-1][square[2][1]-1] == "#" and board[square[3][0]-1][square[3][1]-1] == "#":
            count += 1
    print(count)
