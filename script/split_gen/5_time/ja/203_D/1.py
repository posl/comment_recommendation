def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**9
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            tmp = []
            for k in range(K):
                for l in range(K):
                    tmp.append(A[i + k][j + l])
            tmp.sort()
            ans = min(ans, tmp[(K * K) // 2])
    print(ans)
