def solve():
    N, K = map(int, input().split())
    d = [0] * N
    for _ in range(K):
        A = list(map(int, input().split()))
        for i in range(1, len(A)):
            d[A[i]-1] += 1
    ans = 0
    for i in range(N):
        if d[i] == 0:
            ans += 1
    print(ans)
    return 0

if __name__ == '__main__':
    solve()