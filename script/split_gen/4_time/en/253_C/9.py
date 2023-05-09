def main():
    from collections import Counter
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline
    q = int(input())
    s = []
    s_c = Counter()
    s_max = []
    s_min = []
    s_sum = 0
    for _ in range(q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            s.append(q[1])
            heappush(s_max, -q[1])
            heappush(s_min, q[1])
            s_sum += q[1]
            s_c[q[1]] += 1
        elif q[0] == 2:
            while q[2] > 0 and s_c[q[1]] > 0:
                s_c[q[1]] -= 1
                q[2] -= 1
                s_sum -= q[1]
            while s_max and s_c[-s_max[0]] == 0:
                heappop(s_max)
            while s_min and s_c[s_min[0]] == 0:
                heappop(s_min)
        else:
            print(-s_max[0] - s_min[0])
    return
