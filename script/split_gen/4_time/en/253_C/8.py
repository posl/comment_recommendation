def main():
    from sys import stdin
    input = stdin.readline
    from collections import defaultdict
    import heapq
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    s = []
    d = defaultdict(int)
    for query in queries:
        if query[0] == 1:
            heapq.heappush(s, query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            while query[2] > 0 and s:
                if d[s[0]] >= query[2]:
                    d[s[0]] -= query[2]
                    query[2] = 0
                else:
                    query[2] -= d[s[0]]
                    d[s[0]] = 0
                    heapq.heappop(s)
        else:
            print(max(s) - min(s))
