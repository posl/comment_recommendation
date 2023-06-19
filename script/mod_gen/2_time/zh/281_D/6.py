def solve():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    ans = -1
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if i == 1 and j == 2:
                continue
            if A[i - 1] + A[j - 1] <= D:
                ans = max(ans, A[i - 1] + A[j - 1])
    print(ans)

if __name__ == '__main__':
    solve()