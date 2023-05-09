Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if w / 2 == x and h / 2 == y else 0)

=======
Suggestion 2

def main():
    W,H,x,y = map(int, input().split())
    if W/2 == x and H/2 == y:
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

=======
Suggestion 3

def main():
    w, h, x, y = map(int, input().split())
    area = w*h/2
    if x == w/2 and y == h/2:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 4

def main():
    W, H, x, y = map(int, input().split())
    print(W*H/2, 1 if x*2 == W and y*2 == H else 0)

=======
Suggestion 5

def main():
    w,h,x,y = map(int, input().split())
    if (w/2 == x) and (h/2 == y):
        print(w*h/2, 1)
    else:
        print(w*h/2, 0)

=======
Suggestion 6

def main():
    W,H,x,y = map(int, input().split())
    area = W * H / 2
    if x == W/2 and y == H/2:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 7

def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2,1 if W/2==x and H/2==y else 0)

=======
Suggestion 8

def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    flag = 0

    if x == W / 2 and y == H / 2:
        flag = 1

    print(area, flag)

=======
Suggestion 9

def rectangle(w,h,x,y):
    area = w*h
    if (x == w/2) and (y == h/2):
        return [area/2,1]
    else:
        return [area/2,0]
