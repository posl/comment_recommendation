Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    ans = 0
    if r > 1:
        ans += 1
    if r < h:
        ans += 1
    if c > 1:
        ans += 1
    if c < w:
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(4 if (R == 1 or R == H) and (C == 1 or C == W) else 3 if (R == 1 or R == H) or (C == 1 or C == W) else 2)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(3)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(H * W - (R - 1) * W - (C - 1) * H + (R - 1) * (C - 1))

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(4 if R == 1 or R == H or C == 1 or C == W else 8)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(H*W - (H-R)*W - (W-C)*H + (H-R)*(W-C))

=======
Suggestion 7

def solve():
    H,W = map(int, input().split())
    r,c = map(int, input().split())
    print(2 if r in (1,H) and c in (1,W) else 3 if r in (1,H) or c in (1,W) else 4)
solve()

=======
Suggestion 8

def main():
    h,w = map(int, input().split())
    r,c = map(int, input().split())
    print(h*w-((h-r)*w+(w-c)*h-(h-r)*(w-c)))

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())

    print(h*w - (r*w + c*h - r*c))

=======
Suggestion 10

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W-(H*C+W*R-R*C))
