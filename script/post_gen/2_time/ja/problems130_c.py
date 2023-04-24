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
    W, H, x, y = map(int, input().split())
    print(W * H / 2, 1 if x * 2 == W and y * 2 == H else 0)

=======
Suggestion 3

def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2,end=" ")
    if x*2==W and y*2==H:
        print(1)
    else:
        print(0)

=======
Suggestion 4

def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if 2*x==W and 2*y==H:
        print(area,1)
    else:
        print(area,0)

=======
Suggestion 5

def main():
    W,H,x,y = map(int,input().split())
    if W == x or H == y:
        print(0.5*W*H,0)
    else:
        print(0.5*W*H,1)

=======
Suggestion 6

def main():
    #入力
    W,H,x,y = map(int, input().split())
    #処理
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 7

def main():
    W,H,x,y = map(int,input().split())
    import math
    S = W*H/2
    if x*2 == W and y*2 == H:
        M = 1
    else:
        M = 0
    print(S,M)

=======
Suggestion 8

def solve(W,H,x,y):
    # ここにコードを書く
    return
