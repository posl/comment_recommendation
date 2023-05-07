def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        s = ''.join(sorted(s))
        d[s] = d.get(s, 0) + 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)
