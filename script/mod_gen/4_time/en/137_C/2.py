def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        k = ''.join(sorted(s[i]))
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()