def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i]-K*X, 0)
    return ans
print(solve())

if __name__ == '__main__':
    solve()