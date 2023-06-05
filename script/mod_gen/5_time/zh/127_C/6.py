def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    for i in range(1, N + 1):
        l = 0
        r = 0
        while l < M and L[l] < i:
            l += 1
        while r < M and R[r] < i:
            r += 1
        ans += r - l
    print(ans)

if __name__ == '__main__':
    solve()