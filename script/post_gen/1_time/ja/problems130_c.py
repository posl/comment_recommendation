Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    W, H, x, y = map(int, input().split())
    if x*2 == W and y*2 == H:
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

=======
Suggestion 2

def main():
    W,H,x,y=map(int,input().split())
    if x==W/2 and y==H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 3

def main():
    W,H,x,y=map(int,input().split())
    if x==0 or x==W or y==0 or y==H:
        print(W*H/2,0)
    else:
        print(W*H/2,1)

=======
Suggestion 4

def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    if x == W / 2 and y == H / 2:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 5

def main():
    W,H,x,y = map(int,input().split())
    if W == x*2 and H == y*2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 6

def main():
    W,H,x,y=map(int,input().split())
    S = W*H/2
    if x==W/2 and y==H/2:
        print(S,1)
    else:
        print(S,0)

=======
Suggestion 7

def main():
    W,H,x,y=map(int,input().split())
    ans1=0
    ans2=0
    if x*2==W and y*2==H:
        ans1=W*H/2
        ans2=1
    else:
        ans1=W*H/2
        ans2=0
    print(ans1,ans2)

=======
Suggestion 8

def main():
    W, H, x, y = (int(i) for i in input().split())
    print(W*H/2, 1 if x*2==W and y*2==H else 0)

=======
Suggestion 9

def area(x, y, w, h):
    return x * y + (w - x) * (h - y)

w, h, x, y = map(int, input().split())
print(area(x, y, w, h), int(area(x, y, w, h) == max(area(x, y, w, h), area(x, 0, w, y), area(0, y, x, h), area(x, 0, w, h - y))))

=======
Suggestion 10

def main():
    W,H,x,y = list(map(int,input().split()))
    #最大値を達成する分割の方法が複数あるかも判定する
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)
