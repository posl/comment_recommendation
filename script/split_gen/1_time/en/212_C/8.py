def main():
    import sys
    from bisect import bisect_left
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for a in A:
        idx = bisect_left(B, a)
        if idx == M:
            ans = min(ans, abs(a-B[idx-1]))
        elif idx == 0:
            ans = min(ans, abs(a-B[idx]))
        else:
            ans = min(ans, abs(a-B[idx-1]), abs(a-B[idx]))
    write(str(ans))
