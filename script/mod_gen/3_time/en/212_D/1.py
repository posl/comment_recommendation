def main():
    from heapq import heappush, heappop
    Q = int(input())
    que = []
    offset = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(que, query[1] - offset)
        elif query[0] == 2:
            offset += query[1]
        else:
            print(heappop(que) + offset)

if __name__ == '__main__':
    main()