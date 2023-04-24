Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())

    if h == 1 and w == 1:
        print(0)
    elif h == 1 or w == 1:
        print(1)
    else:
        print(4)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    if H == 1 and W == 1:
        print(0)
    elif H == 1 and W > 1:
        print(2)
    elif H > 1 and W == 1:
        print(1)
    else:
        print(4)

=======
Suggestion 3

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    if H == 1 and W == 1:
        print(0)
    elif H == 1 or W == 1:
        print(1)
    else:
        print(4)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h - 1) * w + (w - 1) * h - 2 * (r - 1) - 2 * (c - 1))

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - R) * (W - C))

main()

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(4 - (R==1) - (R==H) - (C==1) - (C==W))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(4 - (H == 1) - (W == 1) - (R == H) - (C == W))

main()

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H-1)*W + (W-1)*H - (R-1)*W - (C-1)*H + 2)

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    # H,W
    h, w = map(int, input().split())
    # R,C
    r, c = map(int, input().split())
    # 答え
    ans = 0
    # 縦の端
    if r == 1 or r == h:
        ans += 1
    # 横の端
    if c == 1 or c == w:
        ans += 1
    # 縦の端でない
    if r != 1 and r != h:
        ans += 2
    # 横の端でない
    if c != 1 and c != w:
        ans += 2
    # 答えを表示
    print(ans)
