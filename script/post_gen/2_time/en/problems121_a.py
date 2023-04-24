Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print((h - h1) * (w - w1))

main()

=======
Suggestion 3

def main():
    # H: number of rows
    # W: number of columns
    # h: number of rows to be painted in black
    # w: number of columns to be painted in black
    H, W, h, w = map(int, input().split())
    print((H - h) * (W - w))
