def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = max(ans, P * A[i] + Q * A[i] + R * A[i])
    print(ans)

if __name__ == '__main__':
    solve()