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

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if x * 2 == w and y * 2 == h else 0)

=======
Suggestion 3

def main():
    w, h, x, y = map(int, input().split())
    print(w*h/2, 1 if w/2 == x and h/2 == y else 0)

=======
Suggestion 4

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    print(area, 1 if w / 2 == x and h / 2 == y else 0)

=======
Suggestion 5

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    multiple = 0
    if x == w / 2 and y == h / 2:
        multiple = 1
    print(area, multiple)

=======
Suggestion 6

def main():
    W, H, x, y = map(int, input().split())
    print(W*H/2, 1 if 2*x==W and 2*y==H else 0)

=======
Suggestion 7

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    ans = 0
    if x == w / 2 and y == h / 2:
        ans = 1
    print(area, ans)

=======
Suggestion 8

def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    multi = 0
    if x == W / 2 and y == H / 2:
        multi = 1
    print("{0} {1}".format(area, multi))

=======
Suggestion 9

def main():
    W,H,x,y = map(int, input().split())
    print(W*H/2, 1 if W/2 == x and H/2 == y else 0)
