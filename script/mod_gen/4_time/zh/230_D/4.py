def solve():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    l = 0
    r = 0
    while l < N and r < N:
        if L[l] <= R[r]:
            ans += 1
            l += 1
        else:
            ans -= 1
            r += 1
    print(ans)

if __name__ == '__main__':
    solve()