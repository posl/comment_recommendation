def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        ans = 0
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] >= x:
                ans = N - mid
                right = mid - 1
            else:
                left = mid + 1
        print(ans)
