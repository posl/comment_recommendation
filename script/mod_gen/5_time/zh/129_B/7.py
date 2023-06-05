def solve():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 100000000
    for t in range(1, N):
        s1, s2 = 0, 0
        for i in range(t):
            s1 += W[i]
        for i in range(t, N):
            s2 += W[i]
        ans = min(ans, abs(s1 - s2))
    print(ans)

if __name__ == '__main__':
    solve()