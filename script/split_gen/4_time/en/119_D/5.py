def main():
    a, b, q = map(int, input().split())
    s = [-10 ** 20] + [int(input()) for _ in range(a)] + [10 ** 20]
    t = [-10 ** 20] + [int(input()) for _ in range(b)] + [10 ** 20]
    for _ in range(q):
        x = int(input())
        si = bisect.bisect_left(s, x)
        ti = bisect.bisect_left(t, x)
        ans = 10 ** 20
        for j in range(ti - 1, ti + 1):
            for i in range(si - 1, si + 1):
                ans = min(ans, max(s[i] - x, x - t[j]), max(t[j] - x, x - s[i]))
        print(ans)
