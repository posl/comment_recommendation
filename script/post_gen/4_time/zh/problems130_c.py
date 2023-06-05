Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    W,H,x,y = map(int,input().split())
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 3

def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if x*2 == W and y*2 == H:
        print(area,1)
    else:
        print(area,0)

=======
Suggestion 4

def solve():
    W,H,x,y = map(int,input().split())
    if W/2 == x and H/2 == y:
        print(W*H/2,1)
    else:
        print(W*H/2,0)
solve()

=======
Suggestion 5

def get_area(w, h, x, y):
    area = w * h / 2
    if x == w / 2 and y == h / 2:
        return area, 1
    else:
        return area, 0

=======
Suggestion 6

def main():
    W,H,x,y = map(int,input().split())
    if (W/2 == x and H/2 == y):
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 7

def main():
    W,H,x,y = map(int,input().split())
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 8

def main():
    # W, H, x, y = map(int, input().split())
    W, H, x, y = 2, 2, 1, 1
    print(W*H/2, 1 if x*2==W and y*2==H else 0)
    return

=======
Suggestion 9

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    if 2 * x == w and 2 * y == h:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 10

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if w / 2 == x and h / 2 == y else 0)
