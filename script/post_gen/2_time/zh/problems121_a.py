Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - (h*W + w*H - h*w))

=======
Suggestion 2

def main():
    #H行和W列的白色方形单元格
    #h行和w列
    #还会剩下多少个白色单元格？
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    print(H*W - h*W - w*H + h*w)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    print(h * w - (a * w + b * h - a * b))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    h1,w1 = map(int,input().split())
    print(h*w-h1*w-w1*h+h1*w1)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print(h * w - h1 * w - h * w1 + h1 * w1)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    print((h - a) * (w - b))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print(h * w - (h1 * w + (h - h1) * (w - w1)))
