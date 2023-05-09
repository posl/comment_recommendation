def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M, *UV = map(int, read().split())
    UV = [u - 1 for u in UV]
    UV = [UV[2 * i:2 * (i + 1)] for i in range(M)]
    UV = sorted(UV)
    import bisect
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if [i, j] in UV:
                continue
            k = bisect.bisect_left(UV, [i, j])
            if k < M and UV[k][0] == i:
                continue
            l = bisect.bisect_left(UV, [j, i])
            if l < M and UV[l][0] == j:
                continue
            ans += 1
    print(ans)
