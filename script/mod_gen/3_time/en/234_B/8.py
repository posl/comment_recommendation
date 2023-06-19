def main():
    import sys
    from itertools import combinations
    import math
    N = int(sys.stdin.readline())
    points = []
    for i in range(N):
        x,y = map(int,sys.stdin.readline().split())
        points.append((x,y))
    max_len = 0
    for comb in combinations(points,2):
        x1,y1 = comb[0]
        x2,y2 = comb[1]
        len = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if len > max_len:
            max_len = len
    print(max_len)
main()
