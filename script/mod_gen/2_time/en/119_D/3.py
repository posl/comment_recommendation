def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for xi in x:
        si = bisect.bisect_right(s, xi)
        ti = bisect.bisect_right(t, xi)
        ans = 10**20
        for sj in [si-1, si]:
            for tj in [ti-1, ti]:
                ans = min(ans, max(s[sj], t[tj]) - xi)
                ans = min(ans, xi - min(s[sj], t[tj]))
                ans = min(ans, abs(s[sj] - t[tj]) + min(abs(s[sj] - xi), abs(t[tj] - xi)))
        print(ans)

if __name__ == '__main__':
    main()