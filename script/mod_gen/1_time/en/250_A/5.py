def main():
    # read number of rows and columns
    h,w = map(int, input().split(" "))
    # read row and column of the square
    r,c = map(int, input().split(" "))
    # calculate the number of squares that share a side with Square (R, C)
    # there are 4 squares adjacent to Square (R, C)
    # if Square (R, C) is on the edge of the grid, the number of squares is less than 4
    # if Square (R, C) is on the corner of the grid, the number of squares is less than 4
    # if Square (R, C) is at the center of the grid, the number of squares is 4
    # if Square (R, C) is not at the center of the grid, the number of squares is 4
    if (r == 1 and c == 1) or (r == 1 and c == w) or (r == h and c == 1) or (r == h and c == w):
        print(1)
    elif r == 1 or r == h or c == 1 or c == w:
        print(2)
    else:
        print(4)

if __name__ == '__main__':
    main()