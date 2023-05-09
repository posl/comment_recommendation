def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    import heapq
    heap = []
    ans = 0
    for i in range(1, M+1):
        while AB and AB[0][0] == i:
            heapq.heappush(heap, -AB[0][1])
            AB.pop(0)
        if heap:
            ans -= heapq.heappop(heap)
    print(ans)

if __name__ == '__main__':
    main()