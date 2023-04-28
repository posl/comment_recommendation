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

    print(H*W - (h*W + w*H - h*w))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print((h - h1) * (w - w1))

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    H, W = map(int, input().split())
    print(h*w - (H*w + W*h - H*W))

=======
Suggestion 5

def main():

    H, W = map(int, input().split())
    h, w = map(int, input().split())

    print((H-h)*(W-w))

main()

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print(h*w - (h2*w + w2*h - h2*w2))
    return

=======
Suggestion 7

def main():
    h,w = map(int, input().split())
    h2,w2 = map(int, input().split())
    print((h - h2) * (w - w2))

main()
