def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for j in range(Q):
        left = 0
        right = N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] >= x[j]:
                right = mid
            else:
                left = mid
        print(N - right + 1)
