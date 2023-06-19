def main():
    import heapq
    q = int(input())
    a = []
    heap = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
            heapq.heappush(heap, query[1])
        elif query[0] == 2:
            for j in range(len(a)):
                a[j] += query[1]
            heapq.heappush(heap, heap[0]+query[1])
        else:
            print(heapq.heappop(heap))
main()
