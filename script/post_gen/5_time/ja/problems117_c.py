Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    if n >= m:
        print(0)
        exit()
    diff_list = []
    for i in range(m-1):
        diff_list.append(x_list[i+1] - x_list[i])
    diff_list.sort()
    print(sum(diff_list[:m-n]))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    if n >= m:
        print(0)
        exit()
    x_diff = []
    for i in range(m-1):
        x_diff.append(x[i+1]-x[i])
    x_diff = sorted(x_diff)
    ans = 0
    for i in range(m-n):
        ans += x_diff[i]
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    ans = 0
    d = []
    for i in range(m-1):
        d.append(x[i+1]-x[i])
    d.sort(reverse=True)
    for i in range(n-1):
        ans += d[i]
    print(ans)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    if N>=M:
        print(0)
        exit()
    X_dif = []
    for i in range(M-1):
        X_dif.append(X[i+1]-X[i])
    X_dif.sort()
    print(sum(X_dif[:M-N]))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    ans = 0
    for i in range(m-n):
        ans += diff[i]
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
    else:
        diff = []
        for i in range(m-1):
            diff.append(x[i+1]-x[i])
        diff.sort()
        print(sum(diff[:m-n]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    dist = []
    for i in range(m - 1):
        dist.append(x[i + 1] - x[i])
    dist.sort()
    print(sum(dist[:m - n]))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
    else:
        d = []
        for i in range(m-1):
            d.append(x[i+1] - x[i])
        d.sort()
        print(sum(d[:m-n]))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    d = []
    for i in range(m-1):
        d.append(x[i+1]-x[i])
    d.sort()
    print(sum(d[:m-n]))
