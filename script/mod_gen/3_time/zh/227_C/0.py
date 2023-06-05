def solve():
    N = int(input())
    ans = 0
    for a in range(1, int(N ** (1 / 3)) + 1):
        for b in range(a, int((N - a) ** (1 / 2)) + 1):
            c = N - a - b
            if b <= c:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()