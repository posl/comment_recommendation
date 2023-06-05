Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    h1,w1 = map(int,input().split())
    print((h-h1)*(w-w1))

=======
Suggestion 2

def main():
    h,w = map(int,input().split())
    a,b = map(int,input().split())
    print(h*w - (a*w + b*h - a*b))

=======
Suggestion 3

def main():
    H,W = map(int,input().split())
    h,w = map(int,input().split())
    print(H*W - (h*W + w*H - h*w))

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    H,W = map(int,input().split())
    print(h*w-H*W)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H * W - (H * w + W * h - h * w))

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    h2,w2 = map(int,input().split())
    print(h*w-h*w2-h2*w+w2*h2)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())

    print(h*w-h1*w-w1*h+h1*w1)
