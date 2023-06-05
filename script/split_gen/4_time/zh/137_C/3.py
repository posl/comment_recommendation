def main():
    N = int(input())
    s = [input() for i in range(N)]
    d = {}
    for i in range(N):
        s[i] = ''.join(sorted(s[i]))
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)
