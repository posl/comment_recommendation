Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    if H == 1 and W == 1:
        print(0)
    elif H == 1 or W == 1:
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
    elif H == 1 or W == 1:
        print(1)
    else:
        print(2)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - R) + (W - C))

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h - r) * (w - c))

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-1)*W + (W-1)*H - (H-1)*(W-1))

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(2*(H-1) + 2*(W-1) - (R==H) - (C==W))

main()

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(2 * (h + w) - 4 - (r == h) - (c == w))

main()

=======
Suggestion 8

def main():
    H,W = list(map(int, input().split()))
    R,C = list(map(int, input().split()))
    print(H*W - (H+W-1))

=======
Suggestion 9

def check_square(x, y, h, w):
    if (x > 1 and y > 1) and (x < h and y < w):
        return 4
    elif (x > 1 and y > 1) or (x < h and y < w):
        return 3
    else:
        return 2

h, w = map(int, input().split())
r, c = map(int, input().split())
print(check_square(r, c, h, w))
