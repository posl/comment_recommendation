def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]
    d = defaultdict(int)
    d[0] = 1
    d[10**9] = 1
    d_sum = 0
    d_min = 0
    d_max = 10**9
    for q in queries:
        if q[0] == 1:
            d[q[1]] += 1
            d_sum += q[1]
        elif q[0] == 2:
            d[q[1]] -= min(q[2], d[q[1]])
            d_sum -= min(q[2], d[q[1]]) * q[1]
        else:
            print(d_max - d_min)
            d[d_max] -= 1
            d[d_min] -= 1
            d_sum -= d_max
            d_sum += d_min
            if d[d_max] == 0:
                d_max -= 1
            if d[d_min] == 0:
                d_min += 1
            d_sum -= d_max
            d_sum += d_min
