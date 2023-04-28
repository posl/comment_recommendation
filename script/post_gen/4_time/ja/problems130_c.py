Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    w, h, x, y = map(int, input().split())
    if x == w/2 and y == h/2:
        print(w*h/2, 1)
    else:
        print(w*h/2, 0)

=======
Suggestion 2

def main():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, 1 if x * 2 == W and y * 2 == H else 0)

=======
Suggestion 3

def main():
    W,H,x,y = map(int, input().split())
    if x == W/2 and y == H/2:
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

=======
Suggestion 4

def main():
    W, H, x, y = map(int, input().split())
    print(W*H/2, 1 if W/2 == x and H/2 == y else 0)

=======
Suggestion 5

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    print(area, 1 if x * 2 == w and y * 2 == h else 0)

=======
Suggestion 6

def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2,end=" ")
    if x==W/2 and y==H/2:
        print(1)
    else:
        print(0)

=======
Suggestion 7

def main():
    W, H, x, y = map(int, input().split())
    ans = 0
    if x == W/2 and y == H/2:
        ans = 1
    print(W*H/2, ans)

=======
Suggestion 8

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    is_multiple = 0
    if w == x * 2 and h == y * 2:
        is_multiple = 1
    print(area, is_multiple)

=======
Suggestion 9

def main():
    W, H, x, y = map(int, input().split())
    ans1 = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    ans1 = W * H / 2
    if x == W / 2 and y == H / 2:
        ans2 = 1
    else:
        ans2 = 0
    print(ans1, ans2)
