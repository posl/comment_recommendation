def solve():
    N = int(input())
    s = [input() for _ in range(N)]
    s = list(map(lambda x: ''.join(sorted(x)), s))
    from collections import defaultdict
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()