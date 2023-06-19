Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(i, n, a, x, y):
    if i == n:
        return 0
    else:
        ans = 0
        for j in range(a[i]):
            if y[i][j] == 1:
                ans = max(ans, dfs(i+1, n, a, x, y)+1)
            else:
                ans = max(ans, dfs(i+1, n, a, x, y))
        return ans

n = int(input())
a = []
x = []
y = []
for i in range(n):
    a.append(int(input()))
    x.append([])
    y.append([])
    for j in range(a[i]):
        x[i].append(0)
        y[i].append(0)
        x[i][j], y[i][j] = map(int, input().split())

print(dfs(0, n, a, x, y))

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    X = []
    Y = []
    for i in range(N):
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x - 1)
            Y[i].append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if ((i >> X[j][k]) & 1) ^ Y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

solve()

=======
Suggestion 3

def is_honest(i, N, A, xy):
    for j in range(A[i]):
        if xy[i][j][1] == 1:
            if xy[i][j][0] not in honest:
                honest.append(xy[i][j][0])
                is_honest(xy[i][j][0] - 1, N, A, xy)
        else:
            if xy[i][j][0] in honest:
                return False
    return True

N = int(input())
A = []
xy = []
for i in range(N):
    A.append(int(input()))
    xy.append([])
    for j in range(A[i]):
        xy[i].append(list(map(int, input().split())))

max_honest = 0
for i in range(N):
    honest = []
    if is_honest(i, N, A, xy):
        max_honest = max(max_honest, len(honest))

print(max_honest)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for j in range(a[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j], y[i][j] = map(int, input().split())

    ans = 0
    for i in range(1 << n):
        flag = True
        for j in range(n):
            if ((i >> j) & 1):
                for k in range(a[j]):
                    if (((i >> (x[j][k] - 1)) & 1) ^ y[j][k]):
                        flag = False
        if (flag):
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for j in range(a[i]):
            xi, yi = map(int, input().split())
            x[i].append(xi)
            y[i].append(yi)

    ans = 0
    for bits in range(1 << n):
        flag = True
        for i in range(n):
            if bits & (1 << i):
                for j in range(a[i]):
                    if ((bits >> (x[i][j] - 1)) & 1) ^ y[i][j]:
                        flag = False
        if flag:
            ans = max(ans, bin(bits).count('1'))
    print(ans)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        temp_x = []
        temp_y = []
        for j in range(a[i]):
            temp = input().split()
            temp_x.append(int(temp[0]))
            temp_y.append(int(temp[1]))
        x.append(temp_x)
        y.append(temp_y)

    ans = 0
    for i in range(2 ** n):
        honest = []
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                honest.append(j)
        for j in range(len(honest)):
            for k in range(a[honest[j]]):
                if ((i >> (x[honest[j]][k] - 1)) & 1) ^ y[honest[j]][k]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans = max(ans, len(honest))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for j in range(a[i]):
            p, q = map(int, input().split())
            x[i].append(p)
            y[i].append(q)
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(n):
            if i >> j & 1:
                for k in range(a[j]):
                    if i >> (x[j][k] - 1) & 1 != y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for _ in range(a[i]):
            tmp = list(map(int, input().split()))
            x[i].append(tmp[0])
            y[i].append(tmp[1])

    ans = 0
    for i in range(1, 1 << n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> (x[j][k] - 1)) & 1) ^ y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)
