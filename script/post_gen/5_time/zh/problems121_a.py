Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H * W - (H * w + W * h - h * w))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - (h*W + w*H - h*w))

main()

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    a,b = map(int,input().split())
    print(h*w-a*w-b*h+a*b)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))

=======
Suggestion 5

def get_input():
    # H:行数
    # W:列数
    # h:选择的行数
    # w:选择的列数
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    return H, W, h, w

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    h1,w1 = map(int,input().split())
    print(h*w-h1*w-w1*h+h1*w1)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())

    print(h * w - (a * w + b * (h - a)))

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    h1,w1 = map(int,input().split())
    print(h*w-h1*w-w1*h+w1*h1)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    H, W = map(int, input().split())
    print(h * w - H * w - H * w + H * W)

=======
Suggestion 10

def get_input():
    h, w = input().split(" ")
    h = int(h)
    w = int(w)
    h1, w1 = input().split(" ")
    h1 = int(h1)
    w1 = int(w1)
    return h, w, h1, w1
