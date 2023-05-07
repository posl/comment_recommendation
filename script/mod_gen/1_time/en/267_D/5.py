def main():
    import sys
    input = sys.stdin.readline
    from heapq import heapify, heappop, heappush
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (A[i], i)
    B.sort()
    heapify(B)
    C = [0] * N
    for i in range(N):
        C[i] = (A[i], i)
    C.sort(reverse=True)
    heapify(C)
    ans = 0
    for i in range(1, M + 1):
        a, b = heappop(B)
        c, d = heappop(C)
        if a >= c:
            ans += a * i
            heappush(B, (a, b))
        else:
            ans += c * i
            heappush(C, (c, d))
    print(ans)

if __name__ == '__main__':
    main()