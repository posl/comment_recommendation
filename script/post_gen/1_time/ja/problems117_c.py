Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    d = []
    for i in range(m-1):
        d.append(x[i+1]-x[i])
    d.sort()
    print(sum(d[:m-n]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    D = []
    for i in range(M-1):
        D.append(X[i+1]-X[i])
    D.sort()
    print(sum(D[:M-N]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    diff = []
    for i in range(M-1):
        diff.append(X[i+1] - X[i])
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
        exit()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    ans = 0
    for i in range(M-N):
        ans += diff[i]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X = sorted(X)
    ans = 0
    if N >= M:
        print(ans)
        return
    else:
        ans = sum(X[-N:])-sum(X[:M-N])
        print(ans)
        return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    else:
        diff = []
        for i in range(M-1):
            diff.append(X[i+1]-X[i])
        diff.sort()
        print(sum(diff[:M-N]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return

    dx = []
    for i in range(m-1):
        dx.append(x[i+1]-x[i])
    dx.sort()
    print(sum(dx[:m-n]))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(N, M, X)
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    #print(diff)
    ans = sum(diff[:M-N]) if M > N else 0
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    L = [X[i+1] - X[i] for i in range(M-1)]
    #print(L)
    L.sort()
    #print(L)
    print(sum(L[0:M-N]))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(N, M)
    #print(X)
    diff = [X[i + 1] - X[i] for i in range(M - 1)]
    diff.sort()
    #print(diff)
    if N >= M:
        print(0)
    else:
        print(sum(diff[:M - N]))
