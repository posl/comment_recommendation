def main():
    import sys
    from heapq import heappush,heappop
    input = sys.stdin.readline
    Q = int(input())
    heap = []
    add = 0
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            heappush(heap,query[1]-add)
        elif query[0] == 2:
            add += query[1]
        else:
            print(heappop(heap)+add)
    return

if __name__ == '__main__':
    main()