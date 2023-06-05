Synthesizing 10/10 solutions

=======
Suggestion 1

def check(i, n, A, x, y, honest):
    for j in range(A[i]):
        if honest[x[i][j]] != -1 and honest[x[i][j]] != y[i][j]:
            return False
    return True

=======
Suggestion 2

def main():
    n = int(input())
    a = [0] * n
    x = [[0] * n for _ in range(n)]
    y = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i] = int(input())
        for j in range(a[i]):
            x[i][j], y[i][j] = map(int, input().split())
            x[i][j] -= 1
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> x[j][k]) & 1) ^ y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def f(n, a, x, y):
    ans = 0
    for i in range(2**n):
        honest = [0] * n
        for j in range(n):
            if (i >> j) & 1:
                honest[j] = 1

        ok = True
        for j in range(n):
            if honest[j] == 0:
                continue
            for k in range(a[j]):
                if honest[x[j][k] - 1] != y[j][k]:
                    ok = False
        if ok:
            ans = max(ans, sum(honest))
    return ans

=======
Suggestion 5

def solve():
    N = int(input())
    A = []
    x = []
    y = []
    for i in range(N):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            a, b = map(int, input().split())
            x[i].append(a)
            y[i].append(b)
    ans = 0
    for bit in range(1 << N):
        flag = True
        cnt = 0
        for i in range(N):
            if bit & (1 << i):
                cnt += 1
                for j in range(A[i]):
                    if y[i][j] == 1 and not bit & (1 << (x[i][j] - 1)):
                        flag = False
        if flag:
            ans = max(ans, cnt)
    print(ans)

solve()

=======
Suggestion 6

def check(i, n, A, X, Y):
    honest = [0]*n
    honest[i] = 1
    for j in range(n):
        if not honest[j]:
            continue
        for k in range(A[j]):
            if honest[X[j][k]-1] != Y[j][k]:
                return False
    return True

=======
Suggestion 7

def get_input():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        for j in range(a[i]):
            x_tmp, y_tmp = map(int, input().split())
            x.append(x_tmp)
            y.append(y_tmp)
    return n, a, x, y

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        for j in range(a[i]):
            x, y = map(int, input().split())
    ans = 0
    for i in range(2 ** n):
        flag = True
        for j in range(n):
            if i >> j & 1:
                for k in range(a[j]):
                    if (i >> (x - 1)) & 1 ^ y:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 10

def func():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([0] * a[i])
        y.append([0] * a[i])
        for j in range(a[i]):
            x[i][j], y[i][j] = map(int, input().split())

    ans = 0
    for i in range(2 ** n):
        honest = [0] * n
        flag = 1
        for j in range(n):
            if (i >> j) & 1:
                honest[j] = 1
        for j in range(n):
            if honest[j]:
                for k in range(a[j]):
                    if honest[x[j][k] - 1] != y[j][k]:
                        flag = 0
        if flag:
            ans = max(ans, sum(honest))
    print(ans)
