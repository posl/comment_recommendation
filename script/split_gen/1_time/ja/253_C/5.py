def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    import heapq
    hq1 = []
    hq2 = []
    for a in A:
        if a[0] == 1:
            heapq.heappush(hq1, a[1])
            heapq.heappush(hq2, -a[1])
        elif a[0] == 2:
            c = a[2]
            for i in range(c):
                if hq1[0] == a[1]:
                    heapq.heappop(hq1)
                    break
            for i in range(c):
                if -hq2[0] == a[1]:
                    heapq.heappop(hq2)
                    break
        else:
            print(-hq2[0] - hq1[0])
