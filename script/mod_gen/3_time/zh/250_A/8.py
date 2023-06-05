def get_num():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    num = 0
    if H == 1 and W == 1:
        return 0
    elif H == 1:
        if C == 1 or C == W:
            return 1
        else:
            return 2
    elif W == 1:
        if R == 1 or R == H:
            return 1
        else:
            return 2
    else:
        if R == 1 or R == H:
            num += 1
        if C == 1 or C == W:
            num += 1
        return num + 2
print(get_num())
