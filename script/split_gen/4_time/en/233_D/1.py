def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(n + 1):
        ans += d[s[i]]
        d[s[i] + k] += 1
    print(ans)
