Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def distance(x, y):
    return (x**2 + y**2)**0.5

N, D = map(int, input().split())

count = 0
for i in range(N):
    x, y = map(int, input().split())
    if distance(x, y) <= D:
        count += 1
print(count)

=======
Suggestion 2

def problem174_b():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x ** 2 + y ** 2) ** 0.5 <= D:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n,d=map(int,input().split())
    ans=0
    for i in range(n):
        x,y=map(int,input().split())
        if x**2+y**2<=d**2:
            ans+=1
    print(ans)

=======
Suggestion 5

def main():
    n,d = map(int,input().split())
    ans = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2+y**2 <= d**2:
            ans += 1
    print(ans)

main()

=======
Suggestion 6

def main():
    N,D = map(int,input().split())
    count = 0
    for i in range(N):
        x,y = map(int,input().split())
        if (x**2+y**2)**0.5 <= D:
            count += 1
    print(count)

=======
Suggestion 7

def get_distance(x, y):
    return (x**2 + y**2)**(1/2)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        if XY[i][0]**2 + XY[i][1]**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if x**2 + y**2 <= d**2:
            ans += 1
    print(ans)
