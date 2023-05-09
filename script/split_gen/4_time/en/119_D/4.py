def main():
    a, b, q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(a)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(b)] + [10**20]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        si = bisect.bisect_left(s, x[i])
        ti = bisect.bisect_left(t, x[i])
        ans = 10**20
        for j in range(si-1, si+1):
            for k in range(ti-1, ti+1):
                ans = min(ans, max(s[j], t[k]) - x[i])
                ans = min(ans, x[i] - min(s[j], t[k]))
        print(ans)
