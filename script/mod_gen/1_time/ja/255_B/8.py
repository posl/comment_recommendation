def main():
    import sys
    import math
    input = sys.stdin.readline
    #input = open('test.txt', 'r').readline
    from collections import deque
    from collections import defaultdict
    from itertools import product
    from itertools import combinations
    from itertools import permutations
    from bisect import bisect_left
    from bisect import bisect_right
    from heapq import heappush, heappop
    from copy import deepcopy
    from operator import itemgetter
    from functools import reduce
    def calc_dist(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    def is_ok(x, y, r, pos):
        for x2, y2 in pos:
            if calc_dist(x, y, x2, y2) > r:
                return False
        return True
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    pos = [list(map(int, input().split())) for _ in range(N)]
    left = 0
    right = 10 ** 10
    for _ in range(100):
        mid = (left + right) / 2
        if is_ok(0, 0, mid, [pos[i - 1] for i in A]):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()