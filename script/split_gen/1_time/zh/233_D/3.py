def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] += a[i-1]
    ans = 0
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n+1):
        ans += d[a[i]]
        d[a[i]+k] += 1
    print(ans)
