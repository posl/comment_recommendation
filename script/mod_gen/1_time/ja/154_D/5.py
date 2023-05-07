def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    sum_P = sum(P[:K])
    max_sum_P = sum_P
    for i in range(K, N):
        sum_P += P[i] - P[i - K]
        max_sum_P = max(max_sum_P, sum_P)
    print((max_sum_P + K) / 2)

if __name__ == '__main__':
    solve()