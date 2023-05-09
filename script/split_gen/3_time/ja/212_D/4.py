def main():
    import sys
    from heapq import heappush, heappop
    readline = sys.stdin.readline
    Q = int(readline())
    balls = []
    balls_sum = 0
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 1:
            heappush(balls, query[1])
        elif query[0] == 2:
            balls_sum += query[1]
        else:
            print(heappop(balls) + balls_sum)
            balls_sum = 0
