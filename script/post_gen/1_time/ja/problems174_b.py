Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        X, Y = map(int, input().split())
        if X**2 + Y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N,D = map(int,input().split())
    cnt = 0
    for i in range(N):
        x,y = map(int,input().split())
        if x**2+y**2 <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N,D = map(int,input().split())
    cnt = 0
    for i in range(N):
        X,Y = map(int,input().split())
        if X**2 + Y**2 <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N,D = map(int,input().split())
    ans = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if x**2+y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N,D=map(int,input().split())
    ans=0
    for i in range(N):
        x,y=map(int,input().split())
        if (x**2+y**2)**(1/2)<=D:
            ans+=1
    print(ans)

=======
Suggestion 8

def main():
    N,D = map(int,input().split())
    cnt = 0
    for i in range(N):
        x,y = map(int,input().split())
        if (x**2+y**2)**(1/2) <= D:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    N,D = map(int,input().split())
    count = 0
    for i in range(N):
        X,Y = map(int,input().split())
        if (X**2+Y**2)**(1/2) <= D:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    #入力
    N,D = map(int,input().split())
    #座標が入ったリスト
    L = []
    for i in range(N):
        X,Y = map(int,input().split())
        L.append([X,Y])
    #print(L)
    #原点からの距離がD以下であるような点の個数をカウントする
    count = 0
    for i in range(N):
        if (L[i][0]**2 + L[i][1]**2)**0.5 <= D:
            count += 1
    #出力
    print(count)
