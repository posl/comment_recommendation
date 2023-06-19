def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, M, Q = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(M)]
    PQ = [tuple(map(int, input().split())) for _ in range(Q)]
    d = defaultdict(int)
    for l, r in LR:
        d[l] += 1
        d[r+1] -= 1
    for i in range(1, N+1):
        d[i] += d[i-1]
    for p, q in PQ:
        print(d[q]-d[p-1])
main()
