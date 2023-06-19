def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    for i in range(M - 1):
        ans += R[i] - L[i] + 1
    ans += R[M - 1] - L[M - 1] + 1
    print(ans)

if __name__ == '__main__':
    solve()