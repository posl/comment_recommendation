Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem174_b():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x**2 + y**2 <= d**2:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def solve():
    n,d = map(int, input().split())
    ans = 0
    for i in range(n):
        x,y = map(int, input().split())
        if x*x+y*y <= d*d:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x**2+y**2 <= d**2:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n,d = map(int,input().split())
    cnt = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2+y**2 <= d**2:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def problems174_b():
    pass

=======
Suggestion 6

def max_distance():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N,D = map(int,input().split())
    count = 0
    for i in range(N):
        x,y = map(int,input().split())
        if x**2+y**2<=D**2:
            count+=1
    print(count)

=======
Suggestion 8

def problem174_b():
    return

=======
Suggestion 9

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if (x ** 2 + y ** 2) ** 0.5 <= d:
            count += 1
    print(count)
