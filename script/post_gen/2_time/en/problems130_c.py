Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    W, H, x, y = map(int, input().split())
    if x == W/2 and y == H/2:
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

=======
Suggestion 2

def main():
    W,H,x,y = map(int,input().split())
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

main()

=======
Suggestion 3

def main():
    w, h, x, y = map(int, input().split())
    area = w * h / 2
    if x * 2 == w and y * 2 == h:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 4

def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    if W == 2 * x and H == 2 * y:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 5

def main():
    W, H, x, y = map(int, input().split())
    ans = W * H / 2
    if x == W / 2 and y == H / 2:
        print(ans, 1)
    else:
        print(ans, 0)

=======
Suggestion 6

def main():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, 1 if W == x * 2 and H == y * 2 else 0)

=======
Suggestion 7

def main():
    W, H, x, y = map(int, input().split())
    print(W*H/2, 1 if W/2 == x and H/2 == y else 0)

=======
Suggestion 8

def main():
    W,H,x,y=map(int,input().split())
    a = W*H/2
    if W/2 == x and H/2 == y:
        b = 1
    else:
        b = 0
    print(a,b)

=======
Suggestion 9

def f(W,H,x,y):
    if x*2==W and y*2==H:
        return W*H/2,1
    else:
        return W*H/2,0

W,H,x,y=map(int,input().split())
print(*f(W,H,x,y))

=======
Suggestion 10

def cut_rectangle(w,h,x,y):
    max_area = 0
    max_area = max(max_area, x * h)
    max_area = max(max_area, w * y)
    max_area = max(max_area, (w - x) * h)
    max_area = max(max_area, w * (h - y))
    print(max_area, 1 if w == x or h == y else 0)

cut_rectangle(2,3,1,2)
cut_rectangle(2,2,1,1)
cut_rectangle(1000000000,1000000000,0,0)
cut_rectangle(1000000000,1000000000,1000000000,1000000000)
