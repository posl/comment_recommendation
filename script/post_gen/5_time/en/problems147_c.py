Synthesizing 10/10 solutions

=======
Suggestion 1

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
        honest = []
        for j in range(N):
            if i & (1 << j):
                honest.append(j+1)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j]-1]):
                if (Y[honest[j]-1][k] == 1 and X[honest[j]-1][k] not in honest) or (Y[honest[j]-1][k] == 0 and X[honest[j]-1][k] in honest):
                    flag = False
        if flag:
            ans = max(ans, len(honest))
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
        honest = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if Y[j][k] == 1 and (i >> (X[j][k] - 1)) & 1 == 0:
                        honest = False
            else:
                for k in range(A[j]):
                    if Y[j][k] == 0 and (i >> (X[j][k] - 1)) & 1 == 1:
                        honest = False
        if honest:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        x = []
        y = []
        for j in range(A[i]):
            tmp = input().split()
            x.append(int(tmp[0]))
            y.append(int(tmp[1]))
        X.append(x)
        Y.append(y)

    ans = 0
    for i in range(2**N):
        honest = [False] * N
        tmp = i
        for j in range(N):
            if tmp % 2 == 1:
                honest[N-1-j] = True
            tmp //= 2
        flag = True
        for j in range(N):
            if honest[j]:
                for k in range(A[j]):
                    if honest[X[j][k]-1] != bool(Y[j][k]):
                        flag = False
        if flag:
            ans = max(ans, sum(honest))
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = [0] * N
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        A[i] = int(input())
        X[i] = [0] * A[i]
        Y[i] = [0] * A[i]
        for j in range(A[i]):
            X[i][j], Y[i][j] = map(int, input().split())
            X[i][j] -= 1
    ans = 0
    for mask in range(1 << N):
        ok = True
        for i in range(N):
            if mask & (1 << i):
                for j in range(A[i]):
                    if ((mask >> X[i][j]) & 1) ^ Y[i][j]:
                        ok = False
                        break
                if not ok:
                    break
        if ok:
            ans = max(ans, bin(mask).count('1'))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [0] * N
    X = [[] for _ in range(N)]
    Y = [[] for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x - 1)
            Y[i].append(y)
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(N):
            if i >> j & 1:
                for k in range(A[j]):
                    if i >> X[j][k] & 1 != Y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a = int(input())
        for j in range(a):
            x, y = map(int, input().split())
            if y == 1:
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    x = [[None for _ in range(A[i])] for i in range(N)]
    y = [[None for _ in range(A[i])] for i in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if i >> j & 1:
                for k in range(A[j]):
                    if y[j][k] == 1 and i >> (x[j][k] - 1) & 1 == 0:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 8

def check_honesty(x, y, honest):
    for i in range(len(x)):
        if y[i] == 1:
            if honest[x[i]-1] == 0:
                return 0
        else:
            if honest[x[i]-1] == 1:
                return 0
    return 1

=======
Suggestion 9

def get_honest_count(N, A, X, Y):
    honest_count = 0
    for i in range(N):
        if A[i] == 0:
            honest_count += 1
        else:
            honest = True
            for j in range(A[i]):
                if X[i][j] > 0 and Y[i][j] != A[X[i][j] - 1]:
                    honest = False
                    break
            if honest:
                honest_count += 1
    return honest_count

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
print(get_honest_count(N, A, X, Y))

=======
Suggestion 10

def check_honesty(persons, testimony):
    for i in range(len(persons)):
        if persons[i] == 1:
            if testimony[i] != 1:
                return False
    return True
