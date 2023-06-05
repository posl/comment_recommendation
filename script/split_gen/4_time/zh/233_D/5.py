def solve(n, k, a):
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    from collections import Counter
    c = Counter(s)
    for i in range(n + 1):
        ans += c[s[i] + k]
        if s[i] == s[i + 1]:
            c[s[i]] -= 1
    return ans
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
