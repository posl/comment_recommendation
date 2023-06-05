def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        low = 0
        high = N - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] >= x:
                high = mid
            else:
                low = mid + 1
        if A[low] >= x:
            print(N - low)
        else:
            print(N - low - 1)
