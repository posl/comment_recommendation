Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - h*W - w*H + h*w)

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    h,w = map(int,input().split())
    print(H*W - (h*W + w*H - h*w))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print(h*w-h1*w-w1*h+h1*w1)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    print(h * w - (a * w + b * h - a * b))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print(h * w - (h1 * w + (h - h1) * (w - w1)))

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    h,w = map(int,input().split())
    print(H*W - h*W - H*w + h*w)
main()
