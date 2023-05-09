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

if __name__ == '__main__':
    main()