Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())

    if r == 1:
        if c == 1:
            print(0)
        elif c == w:
            print(0)
        else:
            print(1)
    elif r == h:
        if c == 1:
            print(0)
        elif c == w:
            print(0)
        else:
            print(1)
    else:
        if c == 1:
            print(1)
        elif c == w:
            print(1)
        else:
            print(2)

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    count = 0
    if R > 1:
        count += 1
    if R < H:
        count += 1
    if C > 1:
        count += 1
    if C < W:
        count += 1

    print(count)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(4 - (r == 1) - (r == h) - (c == 1) - (c == w))

=======
Suggestion 5

def main():
    # input
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    # compute
    ans = 0

    # output
    print(ans)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    ans = 0
    if r-1 >= 1:
        ans += 1
    if r+1 <= h:
        ans += 1
    if c-1 >= 1:
        ans += 1
    if c+1 <= w:
        ans += 1
    print(ans)

main()

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print(4 if (r==1 or r==h) and (c==1 or c==w) else 3 if (r==1 or r==h) or (c==1 or c==w) else 2)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print("h:{}, w:{}, r:{}, c:{}".format(h, w, r, c))
    print("ans:{}".format((h-r+1)*(w-c+1)))

=======
Suggestion 9

def problems250_a():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(4 if R==1 or R==H or C==1 or C==W else 8)

=======
Suggestion 10

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W - (H-C)*W - (W-R)*H + (H-C)*(W-R))
