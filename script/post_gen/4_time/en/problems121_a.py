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
    print(H * W - (h * W + w * H - h * w))

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
    h2, w2 = map(int, input().split())

    print(h * w - (h2 * w + w2 * h - h2 * w2))

=======
Suggestion 5

def main():
    hw = input()
    hw = hw.split()
    h = int(hw[0])
    w = int(hw[1])
    hw = input()
    hw = hw.split()
    hh = int(hw[0])
    ww = int(hw[1])
    print((h-hh)*(w-ww))
    return 0
