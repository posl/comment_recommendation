Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        if (i+1) in X:
            time += Y[X.index(i+1)]
            if time > T:
                time = T
    print("Yes")

=======
Suggestion 2

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            exit()
        if i+1 in X:
            t += Y[X.index(i+1)]
            if t > T:
                t = T

    print("Yes")

main()

=======
Suggestion 3

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            exit()
        if i+1 in X:
            t += Y[X.index(i+1)]
            if t > T:
                t = T
    print("Yes")

=======
Suggestion 4

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    time = T
    now = 0
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if XY[j][0] == i+1:
                time += XY[j][1]
                break
    print("Yes")

=======
Suggestion 5

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [0] * m
    for i in range(m):
        xy[i] = list(map(int, input().split()))
    for i in range(m):
        t = t - (xy[i][0] - xy[i-1][0]) - xy[i][1]
    if t <= 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    cur = T
    for i in range(N-1):
        cur -= A[i]
        if cur <= 0:
            print('No')
            exit()
        cur += A[i]
        for x, y in XY:
            if i+1 == x:
                cur = min(cur + y, T)
    print('Yes')

=======
Suggestion 7

def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    now = 0
    for x,y in XY:
        now += A[x-1]
        now = min(now+T-y,T)
    now += A[N-2]
    if now >= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for i in range(M)]

    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            exit()
        for j in range(M):
            if XY[j][0] == i+1:
                time += XY[j][1]
                break
        if time > T:
            time = T
    print("Yes")

=======
Suggestion 9

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]
    cur = t
    for i in range(n-1):
        cur -= a[i]
        if cur <= 0:
            print('No')
            exit()
        cur = min(cur + xy[i][1], t)
    print('Yes')

=======
Suggestion 10

def func(n, m, t, a, xy):
    for i in range(n-1):
        t -= a[i]
        if t <= 0:
            return False
        for j in range(m):
            if xy[j][0] == i+1:
                t += xy[j][1]
    return True
