def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        ss = ''.join(sorted(s))
        if ss not in d:
            d[ss] = 1
        else:
            d[ss] += 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()