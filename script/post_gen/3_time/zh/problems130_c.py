Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    w,h,x,y = map(int, input().split())
    if w/2 == x and h/2 == y:
        print(w*h/2, 1)
    else:
        print(w*h/2, 0)

=======
Suggestion 2

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if w == 2 * x and h == 2 * y else 0)

=======
Suggestion 3

def main():
    w,h,x,y = map(int, input().split())
    area = w * h
    half_area = area / 2
    # print(half_area)
    if x == w/2 and y == h/2:
        print(half_area,1)
    else:
        print(half_area,0)

=======
Suggestion 4

def main():
    w,h,x,y = map(int,input().split())
    if x==w/2 and y==h/2:
        print(w*h/2,1)
    else:
        print(w*h/2,0)

=======
Suggestion 5

def main():
    W,H,x,y=map(int,input().split())
    if x==W/2 and y==H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 6

def main():
    w,h,x,y = map(int, input().split())
    print(w*h/2, 1 if (w/2,h/2)==(x,y) else 0)

=======
Suggestion 7

def solve():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, int(2 * x == W and 2 * y == H))

=======
Suggestion 8

def problems130_c():
    #读取输入
    W,H,x,y = map(int,input().split())
    #计算面积
    print(W*H/2,1 if x==W/2 and y==H/2 else 0)

=======
Suggestion 9

def main():
    W,H,x,y = map(int,input().split())
    max_area = W*H/2
    if x == W/2 and y == H/2:
        print(max_area,1)
    else:
        print(max_area,0)

=======
Suggestion 10

def main():
    w,h,x,y = map(int,input().split())
    s1 = w*h/2
    s2 = x*y
    s3 = w*y
    s4 = h*x
    if s1 == s2:
        print(s1,1)
    else:
        print(s1,0)
