Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    H,W = map(int,input().split())
    print((h*w) - (H*w) - (h*W) + (H*W))

=======
Suggestion 2

def main():
    # 標準入力の受け取り
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print(h * w - (h2 * w + w2 * h - h2 * w2))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())

    print((h - h2) * (w - w2))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print(h*w - (h2*w + h*w2 - h2*w2))

=======
Suggestion 6

def problems121_a():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H * W - (h * W + w * H - h * w))

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print((h - h1) * (w - w1))

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - (H*w + W*h - h*w))

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    print(h * w - (a * w + b * h - a * b))
