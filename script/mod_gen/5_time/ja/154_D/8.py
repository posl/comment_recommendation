def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = sum(p[:K])
    ans = p_sum
    for i in range(N-K):
        p_sum = p_sum - p[i] + p[i+K]
        if p_sum > ans:
            ans = p_sum
    print((ans+K)/2)

if __name__ == '__main__':
    solve()