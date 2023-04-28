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
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x)
            Y[i].append(y)
    ans = 0
    for i in range(1 << N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if ((i >> (X[j][k] - 1)) & 1) ^ Y[j][k]:
                        flag = False
                        break
                if not flag:
                    break
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        X.append([])
        Y.append([])
        for j in range(A[i]):
            x, y = [int(_) for _ in input().split()]
            X[i].append(x-1)
            Y[i].append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if i & (1 << j):
                for k in range(A[j]):
                    if Y[j][k] == 1 and i & (1 << X[j][k]):
                        continue
                    elif Y[j][k] == 0 and i & (1 << X[j][k]) == 0:
                        continue
                    else:
                        ok = False
                        break
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

solve()

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

def main():
    N = int(input())
    A = [0]*N
    x = [[0]*N for i in range(N)]
    y = [[0]*N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())

    ans = 0
    for i in range(1<<N):
        flag = True
        for j in range(N):
            if (i>>j)&1:
                for k in range(A[j]):
                    if (i>>(x[j][k]-1))&1 != y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 5

def get_input():
    N = int(input())
    A = []
    xy = []
    for i in range(N):
        A.append(int(input()))
        xy.append([])
        for j in range(A[i]):
            xy[i].append(list(map(int, input().split())))
    return N, A, xy

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    xy = []
    for i in range(N):
        xy.append([list(map(int, input().split())) for _ in range(A[i])])
    ans = 0
    for bit in range(1<<N):
        honest = [0 for _ in range(N)]
        for i in range(N):
            if bit & (1<<i):
                honest[i] = 1
        flag = True
        for i in range(N):
            if honest[i] == 1:
                for j in range(A[i]):
                    if honest[xy[i][j][0]-1] != xy[i][j][1]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(honest))
    print(ans)
    return

=======
Suggestion 7

def check_honesty(honesty, people, testimonies):
    for i in range(people):
        if honesty[i] == 1:
            for testimony in testimonies[i]:
                if honesty[testimony[0]-1] != testimony[1]:
                    return False
    return True

=======
Suggestion 8

def check_honesty(N, A, x, y):
    honest = 0
    for i in range(N):
        if A[i] == 0:
            honest += 1
            continue
        else:
            honest_count = 0
            for j in range(A[i]):
                if y[i][j] == 1 and A[x[i][j]-1] > 0:
                    honest_count += 1
            if honest_count == A[i]:
                honest += 1
    return honest

=======
Suggestion 9

def check_honesty(persons, a, x, y):
    for i in range(a):
        if (y[i] == 1):
            persons[x[i] - 1] = 1
        else:
            if (persons[x[i] - 1] == 1):
                return False
    return True

=======
Suggestion 10

def check_honest(i, honest_list, unkind_list):
    for j in unkind_list:
        if i == j:
            return False
    return True
