Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    W, H, x, y = map(int, input().split())
    if x == W / 2 and y == H / 2:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)

=======
Suggestion 2

def main():
    w,h,x,y = map(int,input().split())
    if x == w/2 and y == h/2:
        print(w*h/2,1)
    else:
        print(w*h/2,0)

=======
Suggestion 3

def main():
    # 读取数据
    W,H,x,y = map(int,input().split())
    # 计算面积
    area = W*H/2
    # 判断是否在中间
    if x*2 == W and y*2 == H:
        print(area,1)
    else:
        print(area,0)

=======
Suggestion 4

def split_rect(W, H, x, y):
    # print(W, H, x, y)
    area = W * H
    if W / 2 == x and H / 2 == y:
        return area / 2, 1
    elif W / 2 == x:
        return max(y * W, (H - y) * W), 0
    elif H / 2 == y:
        return max(x * H, (W - x) * H), 0
    else:
        return max(x * H, (W - x) * H), 0

=======
Suggestion 5

def main():
    w,h,x,y = map(int,input().split())
    s = w*h/2
    if w/2 == x and h/2 == y:
        print(s,1)
    else:
        print(s,0)

=======
Suggestion 6

def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if x == W/2 and y == H/2:
        print(area,1)
    else:
        print(area,0)

=======
Suggestion 7

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if w == 2 * x and h == 2 * y else 0)

=======
Suggestion 8

def main():
    w, h, x, y = map(int, input().split())

    area = w * h / 2
    print(area, end=' ')
    if 2 * x == w and 2 * y == h:
        print(1)
    else:
        print(0)

=======
Suggestion 9

def main():
    w,h,x,y = map(int,input().split())
    print(w*h/2,1 if x==w/2 and y==h/2 else 0)
