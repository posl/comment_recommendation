Synthesizing 10/10 solutions (Duplicates hidden)

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
    W,H,x,y = map(int, input().split())
    area = W*H/2
    print(area, end=' ')
    if x*2 == W and y*2 == H:
        print(1)
    else:
        print(0)

=======
Suggestion 3

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if 2 * x == w and 2 * y == h else 0)

=======
Suggestion 4

def cut(x,y,w,h):
    if x==w/2 and y==h/2:
        return w*h/2
    elif x==w/2:
        return h*x
    elif y==h/2:
        return w*y
    elif x==0 and y==0:
        return w*h/2
    elif x==0:
        return w*h/2
    elif y==0:
        return w*h/2
    else:
        return max(x*h,(w-x)*h,w*y,w*(h-y))

=======
Suggestion 5

def main():
    w,h,x,y = map(int,input().split())
    if (w/2 == x) and (h/2 == y):
        print(w*h/2,1)
    else:
        print(w*h/2,0)

=======
Suggestion 6

def main():
    w,h,x,y = map(int, raw_input().split())
    if (w/2.0 == x) and (h/2.0 == y):
        print w*h/2.0, 1
    else:
        print w*h/2.0, 0

=======
Suggestion 7

def main():
    # W,H,x,y = map(int, input().split())
    # if x==0 or y==0 or x==W or y==H:
    #     print(W*H/2, 1)
    # else:
    #     print(W*H/2, 0)
    W,H,x,y = map(int, input().split())
    if x==0 or y==0 or x==W or y==H:
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

=======
Suggestion 8

def main():
    w,h,x,y = map(int,input().split())

    if x == w/2 and y == h/2:
        print(w*h/2,1)
    else:
        print(w*h/2,0)

=======
Suggestion 9

def solve():
    W, H, x, y = map(int, input().split())
    print(W*H/2, 1 if W/2 == x and H/2 == y else 0)


solve()
