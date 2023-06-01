Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def input_data():
    input_data = []
    N = int(input())
    for i in range(N):
        A = int(input())
        input_data.append(A)
        for j in range(A):
            input_data.append(list(map(int,input().split())))
    return input_data

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        t_x = []
        t_y = []
        for j in range(a[i]):
            tmp = input().split()
            t_x.append(int(tmp[0]))
            t_y.append(int(tmp[1]))
        x.append(t_x)
        y.append(t_y)
    ans = 0
    for i in range(1<<n):
        flag = True
        cnt = 0
        for j in range(n):
            if i>>j & 1:
                cnt += 1
                for k in range(a[j]):
                    if y[j][k] == 1 and not (i>>(x[j][k]-1) & 1):
                        flag = False
                    if y[j][k] == 0 and (i>>(x[j][k]-1) & 1):
                        flag = False
        if flag:
            ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def check_honesty(honesty, N, A, x, y):
    for i in range(N):
        if honesty[i] == 1:
            for j in range(A[i]):
                if y[i][j] == 1 and honesty[x[i][j]-1] == 0:
                    return False
                if y[i][j] == 0 and honesty[x[i][j]-1] == 1:
                    return False
    return True

=======
Suggestion 5

def getPersonNum(n, a, x, y):
    max = 0
    for i in range(2**n):
        flag = True
        for j in range(n):
            if i & (1 << j):
                if not check(j, a, x, y, i):
                    flag = False
                    break
        if flag:
            max = max if max > bin(i).count('1') else bin(i).count('1')
    return max

=======
Suggestion 6

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
    for i in range(2 ** n):
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> (x[j][k] - 1)) & 1) ^ y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 7

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
            x_y = input().split()
            x.append(int(x_y[0]))
            y.append(int(x_y[1]))
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2 ** N):
        honest = []
        dishonest = []
        for j in range(N):
            if (i >> j) & 1:
                honest.append(j + 1)
            else:
                dishonest.append(j + 1)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j] - 1]):
                if Y[honest[j] - 1][k] == 1 and X[honest[j] - 1][k] not in honest:
                    flag = False
                if Y[honest[j] - 1][k] == 0 and X[honest[j] - 1][k] not in dishonest:
                    flag = False
        if flag:
            ans = max(ans, len(honest))
    print(ans)

=======
Suggestion 8

def get_honest_num(N, A, x, y):
    honest_num = 0
    for i in range(2 ** N):
        honest = []
        for j in range(N):
            if ((i >> j) & 1):
                honest.append(j + 1)
        honest_flag = True
        for j in range(N):
            if ((i >> j) & 1):
                for k in range(A[j]):
                    if (y[j][k] == 0):
                        if (x[j][k] not in honest):
                            honest_flag = False
                            break
                    else:
                        if (x[j][k] in honest):
                            honest_flag = False
                            break
            if (not honest_flag):
                break
        if (honest_flag):
            honest_num = max(honest_num, len(honest))
    return honest_num

=======
Suggestion 9

def is_honest(i, n, a, x, y):
    if i == n:
        for j in range(n):
            if a[j] == 1:
                for k in range(a[j]):
                    if y[j][k] == 1:
                        if a[x[j][k]-1] == 1:
                            if y[x[j][k]-1][0] != 1:
                                return False
                        else:
                            if y[x[j][k]-1][0] != 0:
                                return False
        return True
    else:
        a[i] = 1
        if is_honest(i+1, n, a, x, y):
            return True
        a[i] = 0
        if is_honest(i+1, n, a, x, y):
            return True
        return False

n = int(input())
a = [0] * n
x = []
y = []
for i in range(n):
    a[i] = int(input())
    x.append([0] * a[i])
    y.append([0] * a[i])
    for j in range(a[i]):
        x[i][j], y[i][j] = map(int, input().split())
