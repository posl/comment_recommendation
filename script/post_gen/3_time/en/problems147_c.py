Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[] for _ in range(N)]
    Y = [[] for _ in range(N)]
    for i in range(N):
        for _ in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x - 1)
            Y[i].append(y)
    ans = 0
    for bit in range(1 << N):
        flag = True
        for i in range(N):
            if bit & (1 << i):
                for x, y in zip(X[i], Y[i]):
                    if y == 0 and bit & (1 << x):
                        flag = False
                    if y == 1 and not bit & (1 << x):
                        flag = False
        if flag:
            ans = max(ans, bin(bit).count("1"))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x)
            Y[i].append(y)
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(N):
            if (i >> j) & 1 == 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and (i >> (X[j][k] - 1)) & 1 == 0:
                        flag = False
                    if Y[j][k] == 0 and (i >> (X[j][k] - 1)) & 1 == 1:
                        flag = False
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        for _ in range(A[i]):
            x, y = map(int, input().split())
            X[i][x - 1] = y
            Y[i][x - 1] = y
    ans = 0
    for bit in range(1 << N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if (bit >> j) & 1 and X[i][j] == 0:
                    X[i][j] = 1
                if not (bit >> j) & 1 and X[i][j] == 1:
                    X[i][j] = 0
        if all(all(X[i][j] == Y[i][j] for j in range(N)) for i in range(N)):
            ans = max(ans, bin(bit).count("1"))
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                X[i][j] = Y[i][j]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0 for _ in range(N)] for _ in range(N)]
    Y = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][j] = x - 1
            Y[i][j] = y

    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if (i >> X[j][k]) & 1 != Y[j][k]:
                        flag = False
                        break
            if not flag:
                break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = []
    Y = []
    for i in range(N):
        x = []
        y = []
        for _ in range(A[i]):
            x_i, y_i = map(int, input().split())
            x.append(x_i)
            y.append(y_i)
        X.append(x)
        Y.append(y)

    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1:
                        if (i >> (X[j][k] - 1)) & 1 == 0:
                            ok = False
                    else:
                        if (i >> (X[j][k] - 1)) & 1 == 1:
                            ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append([int(x) for x in input().split()])
    ans = 0
    for i in range(2**N):
        honest = []
        for j in range(N):
            if ((i >> j) & 1):
                honest.append(j+1)
        isOK = True
        for j in honest:
            for k in range(A[j-1][0]):
                if A[j-1][2*k+1] == 1:
                    if A[j-1][2*k+2] not in honest:
                        isOK = False
                        break
                else:
                    if A[j-1][2*k+2] in honest:
                        isOK = False
                        break
            if not isOK:
                break
        if isOK:
            ans = max(ans, len(honest))
    print(ans)

=======
Suggestion 7

def solve(N, A, X, Y):
    ans = 0
    for i in range(2**N):
        flag = 1
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1:
                        if (i >> (X[j][k] - 1)) & 1 == 0:
                            flag = 0
                            break
                    else:
                        if (i >> (X[j][k] - 1)) & 1 == 1:
                            flag = 0
                            break
                if flag == 0:
                    break
        if flag == 1:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 8

def check(i, A, x, y, honest):
    for j in range(A[i]):
        if honest[x[i][j] - 1] != y[i][j]:
            return False
    return True

=======
Suggestion 9

def is_honest(n, honest, testimony):
    for i in range(n):
        if honest[i]:
            for x, y in testimony[i]:
                if honest[x-1] != bool(y):
                    return False
    return True

=======
Suggestion 10

def read_int():
    return int(input())
