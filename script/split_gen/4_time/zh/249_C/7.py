def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        t = []
        for j in range(n):
            if i >> j & 1:
                t.append(s[j])
        if len(t) != k:
            continue
        a = set()
        for j in t:
            a |= set(j)
        if len(a) == k:
            ans = max(ans, len(a))
    print(ans)
