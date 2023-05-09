def main():
    N, M, X = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    ans = 10**9
    for i in range(2**N):
        tmp = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += A[j][0]
                for k in range(M):
                    tmp[k] += A[j][k + 1]
        if all(x >= X for x in tmp):
            ans = min(ans, cost)
    print(ans if ans != 10**9 else -1)
    return

if __name__ == '__main__':
    main()