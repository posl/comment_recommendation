def main():
    from collections import defaultdict
    import itertools
    from math import sqrt
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i, j in itertools.combinations(range(n), 2):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        if sqrt(dist).is_integer():
            cnt += 1
    print(cnt)
