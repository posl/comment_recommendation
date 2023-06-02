Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def check(a, x, y, honest):
    for i in range(a):
        if (x[i] in honest) and (y[i] == 1):
            continue
        elif (x[i] in honest) and (y[i] == 0):
            return False
        elif (x[i] not in honest) and (y[i] == 1):
            return False
        elif (x[i] not in honest) and (y[i] == 0):
            continue
    return True

=======
Suggestion 4

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
        honest = [0] * N
        for j in range(N):
            if i & (1 << j):
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j] == 1:
                for k in range(A[j]):
                    if honest[X[j][k]-1] != Y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, sum(honest))
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
        Xi = []
        Yi = []
        for j in range(A[i]):
            x,y = map(int,input().split())
            Xi.append(x)
            Yi.append(y)
        X.append(Xi)
        Y.append(Yi)

    ans = 0
    for i in range(1<<N):
        honest = []
        for j in range(N):
            if i & (1<<j):
                honest.append(j+1)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j]-1]):
                if Y[honest[j]-1][k] == 1 and X[honest[j]-1][k] not in honest:
                    flag = False
                    break
                if Y[honest[j]-1][k] == 0 and X[honest[j]-1][k] in honest:
                    flag = False
                    break
            if flag == False:
                break
        if flag == True:
            ans = max(ans,len(honest))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    A = []
    x = []
    y = []
    for i in range(n):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j], y[i][j] = map(int, input().split())

    ans = 0
    for i in range(2 ** n):
        honest = [False] * n
        for j in range(n):
            if ((i >> j) & 1):
                honest[j] = True
        flag = True
        for j in range(n):
            if honest[j]:
                for k in range(A[j]):
                    if honest[x[j][k] - 1] != y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, honest.count(True))
    print(ans)

=======
Suggestion 7

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
    for i in range(1 << N):
        honest = []
        for j in range(N):
            if i >> j & 1:
                honest.append(j)
        flag = True
        for j in range(len(honest)):
            for k in range(A[honest[j]]):
                if Y[honest[j]][k] == 1 and X[honest[j]][k] not in honest:
                    flag = False
                if Y[honest[j]][k] == 0 and X[honest[j]][k] in honest:
                    flag = False
        if flag:
            ans = max(ans, len(honest))
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = [0]*N
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x,y = map(int,input().split())
            X[i] |= (1<<(x-1))
            Y[i] |= (y<<(x-1))
    #print(A)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(1<<N):
        flag = True
        for j in range(N):
            if i & (1<<j):
                if (i & X[j]) != Y[j]:
                    flag = False
        if flag:
            ans = max(ans,bin(i).count("1"))
    print(ans)

=======
Suggestion 9

def getNumOfHonestPeople(n, statements):
    honestPeople = 0
    for i in range(1, n + 1):
        honestFlag = True
        for j in range(1, n + 1):
            if i in statements[j]:
                if statements[j][0] == i and statements[j][1] == 1:
                    continue
                else:
                    honestFlag = False
                    break
        if honestFlag:
            honestPeople += 1
    return honestPeople
