def solve():
    N = int(input())
    P = list(map(int, input().split()))
    min_p = N + 1
    ans = 0
    for p in P:
        if p <= min_p:
            ans += 1
            min_p = p
    print(ans)

if __name__ == '__main__':
    solve()