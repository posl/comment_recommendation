Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    #print(X)
    if N >= M:
        print(0)
        return
    #print(X)
    d = []
    for i in range(M-1):
        d.append(X[i+1] - X[i])
    #print(d)
    d.sort()
    #print(d)
    ans = 0
    for i in range(M-N):
        ans += d[i]
    print(ans)
    return

=======
Suggestion 2

def solution():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    else:
        X_diff = []
        for i in range(M-1):
            X_diff.append(X[i+1]-X[i])
        X_diff.sort(reverse=True)
        print(sum(X_diff[N-1:]))
        return

solution()

=======
Suggestion 3

def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()

    if N >= M:
        print(0)
        return

    D = []
    for i in range(M-1):
        D.append(X[i+1]-X[i])

    D.sort()
    print(sum(D[:M-N]))

solve()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(abs(x[0]))
    else:
        x_diff = []
        for i in range(m - 1):
            x_diff.append(abs(x[i + 1] - x[i]))
        x_diff.sort()
        print(sum(x_diff[:n - 1]))

=======
Suggestion 5

def main():
    # 输入
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    # 排序
    x.sort()
    # 计算每个点的距离
    diffs = []
    for i in range(m-1):
        diffs.append(x[i+1] - x[i])
    # 排序
    diffs.sort()
    # 计算总和
    sum = 0
    for i in range(m-n):
        sum += diffs[i]
    # 输出
    print(sum)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    #print(x)
    if n == 1:
        print(abs(x[0]-x[m-1]))
        return
    l = []
    for i in range(m-1):
        l.append(x[i+1]-x[i])
    l.sort()
    print(sum(l[:m-n]))

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        return 0
    else:
        Y = []
        for i in range(M-1):
            Y.append(X[i+1]-X[i])
        Y.sort()
        return sum(Y[:M-N])

print(solve())

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()

    if n >= m:
        print(0)
        return

    diff = []
    for i in range(1,m):
        diff.append(x[i]-x[i-1])
    diff.sort()
    ans = sum(diff[:m-n])
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n == 1:
        print(x[m-1]-x[0])
        return
    else:
        l = []
        for i in range(m-1):
            l.append(x[i+1]-x[i])
        l.sort()
        print(sum(l[:m-n]))

=======
Suggestion 10

def main():
    # 读取输入
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    # 排序
    X.sort()
    # 计算相邻两个棋子之间的距离
    dist = []
    for i in range(M-1):
        dist.append(X[i+1] - X[i])
    # 排序
    dist.sort()
    # 计算距离之和
    sum_dist = 0
    for i in dist:
        sum_dist += i
    # 输出
    print(sum_dist - (N-1))
