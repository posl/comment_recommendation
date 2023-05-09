Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - R) * (W - C) + (H - R) * C + R * (W - C))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-R+1)*(W-C+1))

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h * w) - ((h - r) * w) - ((w - c) * r) + ((h - r) * (w - c)))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-R)*(W-C))

=======
Suggestion 5

def get_adjacent_count(h, w, r, c):
    count = 0
    if r > 1:
        count += 1
    if r < h:
        count += 1
    if c > 1:
        count += 1
    if c < w:
        count += 1
    return count

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print( (h - r) * (w - c) )

=======
Suggestion 7

def main():
    h,w = map(int, input().split())
    r,c = map(int, input().split())
    print((h*w)-((h*c)+(w*r)-(r*c)))

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h*w)-((r*w)+(c*h)-(r*c)))

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H*W)-(H+W)+(R*C))
