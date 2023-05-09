def solve():
    N = int(input())
    A = [0] * N
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][j] = x
            Y[i][j] = y
    ans = 0
    for bit in range(1 << N):
        flag = True
        for i in range(N):
            if (bit >> i) & 1:
                for j in range(A[i]):
                    x = X[i][j] - 1
                    y = Y[i][j]
                    if y == 1:
                        if (bit >> x) & 1:
                            continue
                        else:
                            flag = False
                            break
                    elif y == 0:
                        if (bit >> x) & 1:
                            flag = False
                            break
                        else:
                            continue
                if flag == False:
                    break
        if flag:
            ans = max(ans, bin(bit).count("1"))
    print(ans)
