def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (A[i], i)
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += (i + 1) * B[i][0]
    print(ans)
solve()

if __name__ == '__main__':
    solve()