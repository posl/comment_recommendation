def main():
    import sys
    import math
    import itertools
    N = int(sys.stdin.readline())
    xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 順列を列挙
    perm = itertools.permutations(range(1, N))
    # 各順列について、2点間の距離を求める
    ans = 0
    for p in perm:
        d = 0
        for i in range(N-1):
            d += math.sqrt((xy[p[i]][0]-xy[p[i+1]][0])**2 + (xy[p[i]][1]-xy[p[i+1]][1])**2)
        ans += d
    # 平均を求める
    ans = ans / math.factorial(N)
    print(ans)

if __name__ == '__main__':
    main()