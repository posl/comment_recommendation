Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, d, x, y):
    ans = 0
    for i in range(n):
        if x[i] ** 2 + y[i] ** 2 <= d ** 2:
            ans += 1
    return ans

=======
Suggestion 2

def solve():
    N,D = map(int,input().split())
    ans = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if x**2+y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n,d = map(int,input().split())
    count = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2 + y**2 <= d**2:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x*x + y*y <= d*d:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if (x**2 + y**2) <= d**2:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n,d = map(int,input().split())
    cnt = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2 + y**2 <= d**2:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def count_point(n, d, points):
    count = 0
    for i in range(n):
        if points[i][0]**2 + points[i][1]**2 <= d**2:
            count += 1
    return count

=======
Suggestion 8

def main():
    #读入数据
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X * X + Y * Y <= D * D:
            cnt += 1
    print(cnt)
