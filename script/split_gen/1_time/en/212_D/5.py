def main():
    import heapq
    Q = int(input())
    balls = []
    h = []
    heapq.heapify(h)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(h, (query[1], i))
        elif query[0] == 2:
            balls.append((query[1], i))
        else:
            while len(h) > 0:
                if h[0][1] <= i - len(balls):
                    print(heapq.heappop(h)[0])
                    break
                else:
                    heapq.heappop(h)
    for i in range(len(balls)):
        if h[0][1] <= i:
            print(heapq.heappop(h)[0])
        else:
            heapq.heappop(h)
