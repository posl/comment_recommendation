Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - (H*w + W*h - h*w))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    print(h*w - (hh*w + ww*h - hh*ww))

=======
Suggestion 4

def main():
    #input
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    #output
    print((H-h)*(W-w))

=======
Suggestion 5

def main():
    h,w = map(int, input().split())
    a,b = map(int, input().split())
    print((h-a)*(w-b))
