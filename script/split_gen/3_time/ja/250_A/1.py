def solve(H, W, R, C):
    if R == 1 or R == H:
        if C == 1 or C == W:
            return 2
        else:
            return 3
    else:
        if C == 1 or C == W:
            return 3
        else:
            return 4
