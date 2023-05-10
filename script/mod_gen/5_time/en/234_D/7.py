def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    import heapq
    heap = []
    for i in range(n):
        heapq.heappush(heap, p[i])
        if i >= k-1:
            print(heapq.nlargest(k, heap)[-1])

if __name__ == '__main__':
    main()