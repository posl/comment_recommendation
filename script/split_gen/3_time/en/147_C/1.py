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
