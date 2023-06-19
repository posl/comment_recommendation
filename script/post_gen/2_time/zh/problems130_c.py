Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    W,H,x,y = map(int,input().split())
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 2

def solve(w, h, x, y):
    s = w * h / 2
    if (x == w / 2 and y == h / 2):
        return [s, 1]
    else:
        return [s, 0]

=======
Suggestion 3

def solve():
    W, H, x, y = map(int, input().split())
    print(W*H/2, 1 if W/2 == x and H/2 == y else 0)

=======
Suggestion 4

def main():
    w,h,x,y = map(int,input().split())
    print(w*h/2,end=' ')
    if w/2 == x and h/2 == y:
        print(1)
    else:
        print(0)

=======
Suggestion 5

def main():
    W,H,x,y = map(int, input().split())
    print(W*H/2, 1 if W/2 == x and H/2 == y else 0)

=======
Suggestion 6

def solve():
    W,H,x,y = map(int,input().split())
    if x*2 == W and y*2 == H:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 7

def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if x*2 == W and y*2 == H:
        print(area,1)
    else:
        print(area,0)

=======
Suggestion 8

def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2,1 if W==x*2 and H==y*2 else 0)

=======
Suggestion 9

def main():
    w,h,x,y = map(int,input().split())
    if x == w/2 and y == h/2:
        print(w*h/2,1)
    else:
        print(w*h/2,0)
