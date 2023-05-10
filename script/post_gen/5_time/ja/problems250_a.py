Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    print(4)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    if R == 1 or R == H:
        ans += 1
    if C == 1 or C == W:
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    answer = 0
    if R == 1 and C == 1:
        answer = 0
    elif R == 1 and C == W:
        answer = 0
    elif R == H and C == 1:
        answer = 0
    elif R == H and C == W:
        answer = 0
    elif R == 1:
        answer = 1
    elif R == H:
        answer = 1
    elif C == 1:
        answer = 1
    elif C == W:
        answer = 1
    else:
        answer = 2
    print(answer)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(f(h, w, r, c))

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    ans = 0
    if R != 1:
        ans += 1
    if R != H:
        ans += 1
    if C != 1:
        ans += 1
    if C != W:
        ans += 1
    print(ans)

=======
Suggestion 6

def answer(h,w,r,c):
    if r == 1 or r == h:
        if c == 1 or c == w:
            return 2
        else:
            return 3
    else:
        if c == 1 or c == w:
            return 3
        else:
            return 4

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    print((H-R+1)*(W-C+1))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(h*w - (h*c + w*r - r*c))

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 10

def main():
    # 標準入力からH,Wを取得する
    H,W = map(int, input().split())
    # 標準入力からR,Cを取得する
    R,C = map(int, input().split())
    # 出力
    print(H,W,R,C)
