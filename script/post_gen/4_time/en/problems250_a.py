Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - 1) * (W - 1) - (H - R) * (W - C))
    return

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h - r) * (w - c))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(2 * (h - 1) + 2 * (w - 1) - (r == 1) - (r == h) - (c == 1) - (c == w))

=======
Suggestion 4

def main():
    h, w, r, c = map(int, input().split())
    print((r > 1) + (r < h) + (c > 1) + (c < w))

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-R) + (W-C) + 1)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-1)*w + (w-1)*h - (r-1)*(w-1) - (c-1)*(h-1))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(2 * (H + W - 2) - (H == 1 or W == 1))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-1)+(w-1)+(h-1)*(w-1)-2*(r-1)-2*(c-1))

main()

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-1)*(W-1) + (H-1)+(W-1) - 2*min(R-1, H-R) - 2*min(C-1, W-C))

=======
Suggestion 10

def main():
    # H, W, R, C = map(int, input().split())

    # print(4 - (H == R) - (W == C))

    # H, W, R, C = map(int, input().split())
    # print(4 - (H == R) - (W == C))

    H, W, R, C = map(int, input().split())
    print(4 - (H == R) - (W == C))
