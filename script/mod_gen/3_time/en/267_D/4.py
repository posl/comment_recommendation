def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A, reverse=True)
    ans = 0
    for i in range(M):
        ans += B[i] * (i + 1)
    print(ans)
solve()

if __name__ == '__main__':
    solve()