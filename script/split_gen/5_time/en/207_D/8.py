def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    import math
    import itertools
    import heapq
    from collections import deque
    from collections import defaultdict
    from collections import Counter
    N = int(readline())
    S = [list(map(int, readline().split())) for _ in range(N)]
    T = [list(map(int, readline().split())) for _ in range(N)]
    def rotate(s, p):
        x, y = s
        rad = math.radians(p)
        return [x*math.cos(rad) - y*math.sin(rad), x*math.sin(rad) + y*math.cos(rad)]
    for i in range(N):
        for j in range(N):
            if S[i] == T[j]:
                for p in range(360):
                    for q in range(-100, 101):
                        for r in range(-100, 101):
                            tmp = [rotate(s, p) for s in S]
                            tmp = [[s[0]+q, s[1]+r] for s in tmp]
                            if tmp == T:
                                print("Yes")
                                exit()
    print("No")
