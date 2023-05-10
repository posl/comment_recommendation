def main():
    import sys
    import bisect
    readline = sys.stdin.readline
    n, m = map(int, readline().split())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    a.sort()
    b.sort()
    ans = float('inf')
    for i in a:
        idx = bisect.bisect_left(b, i)
        if idx < m:
            ans = min(ans, abs(i - b[idx]))
        if idx > 0:
            ans = min(ans, abs(i - b[idx - 1]))
    print(ans)
