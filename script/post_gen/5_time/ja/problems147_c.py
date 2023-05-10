Synthesizing 10/10 solutions

=======
Suggestion 1

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
    for i in range(2**n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if y[j][k] != ((i >> (x[j][k]-1)) & 1):
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 2

def check(honest, N, A, x, y):
    for i in range(N):
        if (honest >> i) & 1:
            for j in range(A[i]):
                if (((honest >> (x[i][j] - 1)) & 1) ^ y[i][j]) != 0:
                    return False
    return True

=======
Suggestion 3

def get_input():
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
    return n, a, x, y

=======
Suggestion 4

def check(x, y, n):
    for i in range(n):
        if (x>>i)&1:
            for j in range(len(y[i])):
                if (y[i][j]>>i)&1 != (x>>i)&1:
                    return False
    return True

n = int(input())
a = []
y = []
for i in range(n):
    a.append(int(input()))
    y.append([])
    for j in range(a[i]):
        x, y[i][j] = map(int, input().split())
        y[i][j] -= 1
ans = 0
for i in range(1<<n):
    if check(i, y, n):
        ans = max(ans, bin(i).count('1'))
print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        x = []
        y = []
        for j in range(A[i]):
            xj, yj = map(int, input().split())
            x.append(xj)
            y.append(yj)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2 ** N):
        honest = []
        for j in range(N):
            if ((i >> j) & 1):
                honest.append(j)
        flag = True
        for j in honest:
            for k in range(A[j]):
                if (((i >> (X[j][k] - 1)) & 1) ^ Y[j][k]):
                    flag = False
        if flag:
            ans = max(ans, len(honest))
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        a = int(input())
        A.append(a)
        x = []
        y = []
        for j in range(a):
            _x, _y = map(int, input().split())
            x.append(_x)
            y.append(_y)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if i & (1 << j):
                for k in range(A[j]):
                    if Y[j][k] == 1 and not i & (1 << (X[j][k] - 1)):
                        ok = False
                    if Y[j][k] == 0 and i & (1 << (X[j][k] - 1)):
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [0] * n
    x = [[] for _ in range(n)]
    y = [[] for _ in range(n)]
    for i in range(n):
        a[i] = int(input())
        for j in range(a[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j], y[i][j] = map(int, input().split())
            x[i][j] -= 1
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if (((i >> x[j][k]) & 1) ^ y[j][k]) == 0:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
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
            x[i].append(0)
            y[i].append(0)
            x[i][j], y[i][j] = map(int, input().split())

    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if y[j][k] == 1 and not ((i >> (x[j][k] - 1)) & 1):
                        flag = False
                    if y[j][k] == 0 and (i >> (x[j][k] - 1)) & 1:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        x = []
        y = []
        for j in range(A[i]):
            xj, yj = map(int, input().split())
            x.append(xj)
            y.append(yj)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and not (i >> (X[j][k] - 1)) & 1:
                        flag = False
                    if Y[j][k] == 0 and (i >> (X[j][k] - 1)) & 1:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 10

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
    for i in range(1, 2**n):
        flag = True
        for j in range(n):
            if i & (1 << j):
                for k in range(a[j]):
                    if y[j][k] == 1 and not i & (1 << (x[j][k]-1)):
                        flag = False
                        break
                    elif y[j][k] == 0 and i & (1 << (x[j][k]-1)):
                        flag = False
                        break
            if not flag:
                break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
