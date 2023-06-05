def get_num(H, W, R, C):
    if R == 1 and C == 1:
        return 0
    elif R == 1 and C == W:
        return 0
    elif R == H and C == 1:
        return 0
    elif R == H and C == W:
        return 0
    elif R == 1 or R == H:
        return 1
    elif C == 1 or C == W:
        return 1
    else:
        return 2
H, W = map(int, input().split())
R, C = map(int, input().split())
print(get_num(H, W, R, C))
