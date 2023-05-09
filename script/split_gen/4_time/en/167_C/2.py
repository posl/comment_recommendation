def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    ans = 9999999999999999
    for i in range(2**N):
        tmp = 0
        tmpA = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                tmp += C[j]
                for k in range(M):
                    tmpA[k] += A[j][k]
        if min(tmpA) >= X:
            ans = min(ans, tmp)
    if ans == 9999999999999999:
        print(-1)
    else:
        print(ans)
