def main():
    import sys
    import heapq
    input = sys.stdin.readline
    Q = int(input())
    S = []
    heapq.heapify(S)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(S, query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])
        else:
            print(heapq.nlargest(1, S)[0] - heapq.nsmallest(1, S)[0])
