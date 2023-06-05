def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append([a, b])
    ab.sort(key=lambda x: x[0])
    import heapq
    import bisect
    ans = 0
    heap = []
    for i in range(1, m+1):
        while ab and ab[0][0] <= i:
            a, b = ab.pop(0)
            heapq.heappush(heap, -b)
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)
