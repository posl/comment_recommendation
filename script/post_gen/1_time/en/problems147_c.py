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
    for i in range(2 ** N):
        honest = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                honest[j] = 1
        ok = True
        for j in range(N):
            if honest[j] == 0:
                continue
            for k in range(A[j]):
                if honest[X[j][k] - 1] != Y[j][k]:
                    ok = False
        if ok:
            ans = max(ans, sum(honest))
    print(ans)

=======
Suggestion 2

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
            x[i].append([])
            y[i].append([])
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(n):
            if (i>>j)&1:
                for k in range(a[j]):
                    if (i>>(x[j][k]-1))&1 != y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 3

def get_input():
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
    return N, A, X, Y

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    xy = []
    for i in range(n):
        a.append(int(input()))
        xy.append([])
        for j in range(a[i]):
            xy[i].append(list(map(int, input().split())))
    ans = 0
    for i in range(1 << n):
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> (xy[j][k][0] - 1)) & 1) ^ xy[j][k][1]:
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
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    x = []
    y = []
    for i in range(n):
        x.append([])
        y.append([])
        for j in range(a[i]):
            xx, yy = map(int, input().split())
            x[i].append(xx)
            y[i].append(yy)

    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(n):
            if (i>>j)&1:
                for k in range(a[j]):
                    if ((i>>(x[j][k]-1))&1) != y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i)[2:].count("1"))
    print(ans)

=======
Suggestion 6

def solve():
    # write your code here
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = []
    Y = []
    for i in range(N):
        x = []
        y = []
        for _ in range(A[i]):
            _x, _y = map(int, input().split())
            x.append(_x)
            y.append(_y)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if ((i >> (X[j][k] - 1)) & 1) != Y[j][k]:
                        ok = False
                        break
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)
solve()

=======
Suggestion 7

def check_honest(n, a, x, y):
    for i in range(n):
        if a[i] == 0:
            continue
        for j in range(a[i]):
            if y[i][j] == 1:
                if a[x[i][j]-1] == 0:
                    continue
                else:
                    if y[x[i][j]-1][a[x[i][j]-1]-1] == 1:
                        continue
                    else:
                        return False
            else:
                if a[x[i][j]-1] == 0:
                    continue
                else:
                    if y[x[i][j]-1][a[x[i][j]-1]-1] == 0:
                        continue
                    else:
                        return False
    return True

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
    tmp = []
    for j in range(n):
        tmp.append((i>>j)&1)
    tmp.reverse()
    tmp_ans = 0
    for j in range(n):
        if tmp[j] == 1:
            tmp_ans += 1
    if tmp_ans <= ans:
        continue
    if check_honest(n, tmp, x, y):
        ans = tmp_ans
print(ans)

=======
Suggestion 8

def get_honest_persons(N, A, X, Y):
    honest_persons = 0
    for i in range(N):
        honest = True
        for j in range(A[i]):
            if Y[i][j] == 1 and Y[X[i][j]-1][X[X[i][j]-1].index(i+1)] == 0:
                honest = False
        if honest:
            honest_persons += 1
    return honest_persons

=======
Suggestion 9

def dfs(i, x, y):
    if i == n:
        for j in range(n):
            if x[j] == 1:
                for k in range(a[j]):
                    if x[b[j][k]-1] != y[j][k]:
                        return 0
        return sum(x)
    else:
        x[i] = 1
        if dfs(i+1, x, y) == 0:
            x[i] = 0
            return dfs(i+1, x, y)
        else:
            return dfs(i+1, x, y)

n = int(input())
a = [0]*n
b = [[] for i in range(n)]
y = [[] for i in range(n)]
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        x, y[i][j] = map(int, input().split())
        b[i].append(x)
x = [0]*n
print(dfs(0, x, y))

=======
Suggestion 10

def check_honesty(people, i, honest_list):
    if i in honest_list:
        return True
    else:
        for j in range(len(people[i])):
            if people[i][j][1] == 1:
                if not check_honesty(people, people[i][j][0] - 1, honest_list):
                    return False
            else:
                if check_honesty(people, people[i][j][0] - 1, honest_list):
                    return False
        return True
