def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * sum(A[i+1:])
    print(ans % (10**9+7))

if __name__ == '__main__':
    solve()