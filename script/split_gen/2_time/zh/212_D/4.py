def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappush, heappop
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    bag = []
    add = 0
    for p, x in query:
        if p == 1:
            heappush(bag, x - add)
        elif p == 2:
            add += x
        else:
            print(heappop(bag) + add)
