Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,d = map(int,input().split())
    count = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2+y**2 <= d**2:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n, d = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for x, y in l:
        if x**2 + y**2 <= d**2:
            cnt += 1
    print(cnt)

main()

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if d >= (x ** 2 + y ** 2) ** (1 / 2):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x*x + y*y <= D*D:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n,d = map(int,input().split())
    ans = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x*x+y*y <= d*d:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X**2 + Y**2 <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x * x + y * y <= d * d:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n,d = map(int,input().split())
    count = 0
    for i in range(n):
        x,y = map(int,input().split())
        if (x**2+y**2)**0.5 <= d:
            count += 1
    print(count)
