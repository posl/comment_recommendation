def solve():
    N = int(input())
    d = {}
    for i in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)
solve()

if __name__ == '__main__':
    solve()