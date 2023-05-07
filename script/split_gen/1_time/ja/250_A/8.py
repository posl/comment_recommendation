def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    #H,W,R,C = 3,4,2,2
    #H,W,R,C = 3,4,1,3
    #H,W,R,C = 3,4,3,4
    #H,W,R,C = 1,10,1,5
    #H,W,R,C = 8,1,8,1
    #H,W,R,C = 1,1,1,1
    #R,C = 2,2
    #R,C = 1,3
    #R,C = 3,4
    #R,C = 1,5
    #R,C = 8,1
    #R,C = 1,1
    #print(H, W, R, C)
    if H == 1 and W == 1:
        print(0)
    elif H == 1:
        print(1)
    elif W == 1:
        print(1)
    elif R == 1 and C == 1:
        print(2)
    elif R == 1 and C == W:
        print(2)
    elif R == H and C == 1:
        print(2)
    elif R == H and C == W:
        print(2)
    elif R == 1:
        print(3)
    elif R == H:
        print(3)
    elif C == 1:
        print(3)
    elif C == W:
        print(3)
    else:
        print(4)
