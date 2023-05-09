def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    q = []
    for i in range(1, m + 1):
        while ab and ab[0][0] <= i:
            _, b = ab.pop(0)
            heapq.heappush(q, -b)
        if q:
            ans += -heapq.heappop(q)
    print(ans)
