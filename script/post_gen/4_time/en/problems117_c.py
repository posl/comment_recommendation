Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    if N >= M:
        print(0)
    else:
        print(sum(diff[:M-N]))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    print(sum(diff[:max(0, m-n)]))

=======
Suggestion 3

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
        print(sum(diff[0:m-n]))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = []
    for i in range(m-1):
        d.append(x[i+1]-x[i])
    d.sort()
    print(sum(d[:m-n]))

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    print(sum(diff[:M-N]))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    dist = []
    for i in range(m-1):
        dist.append(x[i+1]-x[i])
    dist.sort()
    print(sum(dist[:m-n]))

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    ans = sum(diff[0:M-N])
    print(ans)
solve()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()

    diff = []
    for i in range(M-1):
        diff.append(abs(X[i+1]-X[i]))

    diff.sort(reverse=True)
    print(sum(diff[N-1:]))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    x = sorted(map(int,input().split()))
    if n >= m:
        print(0)
        return
    if n == 1:
        print(max(x) - min(x))
        return
    x = sorted([x[i+1] - x[i] for i in range(m-1)])
    print(sum(x[:m-n]))

=======
Suggestion 10

def process():
    N, M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()

    if N >= M:
        return 0

    dist = []
    for i in range(M-1):
        dist.append(X[i+1]-X[i])

    dist.sort(reverse=True)
    return sum(dist[N-1:])

print(process())
