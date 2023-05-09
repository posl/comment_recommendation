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
        cnt = [0] * 26
        for j in range(k):
            for c in t[j]:
                cnt[ord(c) - ord('a')] += 1
        if max(cnt) <= k:
            ans = max(ans, sum(cnt))
    print(ans)

if __name__ == '__main__':
    main()