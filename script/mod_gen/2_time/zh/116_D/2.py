def solve():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(l, N):
            if h[i] == 0:
                r = i - 1
                break
            elif i == N - 1:
                r = N - 1
                break
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    solve()