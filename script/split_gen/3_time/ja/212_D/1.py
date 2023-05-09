def main():
    import heapq
    Q = int(input())
    que = []
    heapq.heapify(que)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(que, query[1])
        elif query[0] == 2:
            que = [x + query[1] for x in que]
        else:
            print(heapq.heappop(que))
