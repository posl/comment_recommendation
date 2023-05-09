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
