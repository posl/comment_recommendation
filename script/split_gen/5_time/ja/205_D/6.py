def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    from bisect import bisect_left
    N, Q = map(int, readline().split())
    A = list(map(int, readline().split()))
    K = [int(readline()) for _ in range(Q)]
    for i in range(Q):
        k = K[i]
        idx = bisect_left(A, k)
        if idx == 0:
            print(k)
        else:
            print(k+idx)
