def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        key = ''.join(sorted(s))
        d[key] = d.get(key, 0) + 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)
