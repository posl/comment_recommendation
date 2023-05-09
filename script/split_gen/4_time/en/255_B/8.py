def main():
    import sys
    import math
    import itertools
    readline = sys.stdin.readline
    #input
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    XY = [tuple(map(int, readline().split())) for _ in range(N)]
    #solve
    def dist(x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    ans = float('inf')
    for comb in itertools.combinations(A, K):
        tmp = 0
        for x, y in XY:
            tmp = max(tmp, min(dist(x, y, XY[i-1][0], XY[i-1][1]) for i in comb))
        ans = min(ans, tmp)
    #output
    print(ans)
