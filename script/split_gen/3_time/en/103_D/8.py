def main():
    from sys import stdin
    from bisect import bisect_left
    from collections import defaultdict
    N, M = map(int, stdin.readline().split())
    bridges = defaultdict(list)
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        bridges[a].append(b)
        bridges[b].append(a)
    for k, v in bridges.items():
        bridges[k] = sorted(v)
    ans = 0
    for i in range(1, N+1):
        for j in bridges[i]:
            if i < j:
                ans += 1
                bridges[j].pop(bisect_left(bridges[j], i))
    print(ans)
