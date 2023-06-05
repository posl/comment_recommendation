def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] += a[i-1]
    a.insert(0, 0)
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(1, n+2):
        ans += d[a[i]-k]
        d[a[i]] += 1
    print(ans)
