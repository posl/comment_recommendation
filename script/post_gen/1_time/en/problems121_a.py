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

=======
Suggestion 3

def main():
    H,W,h,w = map(int,input().split())
    print((H-h)*(W-w))

=======
Suggestion 4

def paint(h, w, H, W):
    return (H - h) * (W - w)

=======
Suggestion 5

def solve(h,w):
    print(h*w - h - w + 1)

h,w = map(int, input().split())
solve(h,w)
