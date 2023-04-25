Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = [X[i+1] - X[i] for i in range(M-1)]
    D.sort()
    print(sum(D[:max(0, M-N)]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    X.sort()
    d = [0] * (M - 1)
    for i in range(M - 1):
        d[i] = X[i + 1] - X[i]
    d.sort(reverse=True)

    ans = 0
    for i in range(N - 1, M - 1):
        ans += d[i]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    diff = [X[i+1] - X[i] for i in range(M-1)]
    diff.sort()
    print(sum(diff[:M-N]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
    else:
        diff = [X[i+1] - X[i] for i in range(M-1)]
        diff.sort()
        print(sum(diff[:M-N]))

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    ans = sum(diff[:M-N])
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    dist = [abs(x[i + 1] - x[i]) for i in range(m - 1)]
    dist.sort()
    ans = sum(dist[:max(m - n, 0)])
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    else:
        D = []
        for i in range(M-1):
            D.append(X[i+1]-X[i])
        D.sort(reverse=True)
        print(sum(D[N-1:]))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    if N >= M:
        print(0)
    else:
        D = sorted([X[i+1] - X[i] for i in range(M-1)], reverse=True)
        print(sum(D[N-1:]))
