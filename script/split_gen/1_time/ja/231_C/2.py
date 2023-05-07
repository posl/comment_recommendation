def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        left = -1
        right = N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] > x[i]:
                right = mid
            else:
                left = mid
        print(N - right)
