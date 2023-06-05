def solve():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = K
    for a, b in AB:
        if a <= ans:
            ans += b
    print(ans)

if __name__ == '__main__':
    solve()