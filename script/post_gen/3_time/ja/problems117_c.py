Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(m - 1):
        diff.append(x[i + 1] - x[i])
    diff.sort()
    ans = 0
    for i in range(m - n):
        ans += diff[i]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()

    if N >= M:
        print(0)
        return

    if N == 1:
        print(X[-1] - X[0])
        return

    d = []
    for i in range(M - 1):
        d.append(X[i + 1] - X[i])

    d.sort()

    print(sum(d[0:M - N]))

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    L = []
    for i in range(M-1):
        L.append(X[i+1]-X[i])
    L.sort()
    ans = 0
    for i in range(M-N):
        ans += L[i]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    dist = []
    for i in range(M - 1):
        dist.append(X[i + 1] - X[i])
    dist.sort(reverse=True)
    print(sum(dist[N - 1:]))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return

    dist = []
    for i in range(M-1):
        dist.append(X[i+1] - X[i])
    dist.sort()

    print(sum(dist[:M-N]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    diff = []
    for i in range(M-1):
        diff.append(abs(X[i]-X[i+1]))
    #print(diff)
    diff.sort()
    #print(diff)
    if N >= M:
        print(0)
    else:
        print(sum(diff[:M-N]))

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    else:
        diff = []
        for i in range(1,m):
            diff.append(x[i] - x[i-1])
        diff.sort()
        print(sum(diff[:m-n]))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    sub = []
    for i in range(m-1):
        sub.append(x[i+1]-x[i])
    sub.sort()
    print(sum(sub[:m-n]))

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        return 0
    else:
        d = [X[i+1] - X[i] for i in range(M-1)]
        d.sort(reverse=True)
        return sum(d[N-1:])
    
print(solve())

=======
Suggestion 10

def solve():
    n,m = map(int, input().split())
    if n == 1:
        return 0
    if n == 2:
        return 1
    x = list(map(int, input().split()))
    x.sort()
    d = [0]*(m-1)
    for i in range(m-1):
        d[i] = x[i+1] - x[i]
    d.sort()
    return sum(d[:m-n])

print(solve())
