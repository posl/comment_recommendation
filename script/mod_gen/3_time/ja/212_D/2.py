def main():
    import heapq
    q = int(input())
    a = []
    heapq.heapify(a)
    total = 0
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            heapq.heappush(a,query[1]-total)
        elif query[0] == 2:
            total += query[1]
        else:
            print(heapq.heappop(a)+total)

if __name__ == '__main__':
    main()