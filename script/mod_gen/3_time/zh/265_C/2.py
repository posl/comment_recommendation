def path(H,W,G):
    i,j = 1,1
    while True:
        if G[i-1][j-1] == "U":
            if i == 1:
                return [i,j]
            else:
                i -= 1
        elif G[i-1][j-1] == "D":
            if i == H:
                return [i,j]
            else:
                i += 1
        elif G[i-1][j-1] == "L":
            if j == 1:
                return [i,j]
            else:
                j -= 1
        elif G[i-1][j-1] == "R":
            if j == W:
                return [i,j]
            else:
                j += 1
        else:
            return [-1,-1]

if __name__ == '__main__':
    path()