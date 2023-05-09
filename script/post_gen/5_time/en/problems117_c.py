Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1] - X[i])
    diff.sort()
    print(sum(diff[:M-N]))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(m-1):
        diff.append(x[i+1] - x[i])
    diff.sort()
    if n >= m:
        print(0)
    else:
        print(sum(diff[:(m-n)]))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = [0] * (m - 1)
    for i in range(m - 1):
        diff[i] = x[i + 1] - x[i]
    diff.sort()
    print(sum(diff[:max(0, m - n)]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    dist = [0]*(M-1)
    for i in range(M-1):
        dist[i] = X[i+1]-X[i]
    dist.sort()
    print(sum(dist[:max(M-N, 0)]))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    x = sorted(map(int, input().split()))
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff = sorted(diff, reverse=True)
    print(sum(diff[n-1:]))

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    l = []
    for i in range(m-1):
        l.append(x[i+1]-x[i])
    l.sort(reverse=True)
    print(sum(l[n-1:]))

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    d = [0] * (M-1)
    for i in range(M-1):
        d[i] = X[i+1] - X[i]
    d.sort()
    print(sum(d[:max(0, M-N)]))
solve()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    if N >= M:
        print(0)
        return
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    print(sum(diff[:M-N]))

main()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    else:
        d = []
        for i in range(m-1):
            d.append(x[i+1] - x[i])
        d.sort()
        print(sum(d[:m-n]))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    if N >= M:
        print(0)
    else:
        diff = [0] * (M-1)
        for i in range(M-1):
            diff[i] = X[i+1] - X[i]
        diff.sort()
        print(sum(diff[:M-N]))
