def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    X = [int(input()) for _ in range(Q)]
    X.sort()
    for x in X:
        left = 0
        right = N - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < x:
                left = mid + 1
            else:
                right = mid
        if A[left] < x:
            print(N)
        else:
            print(left)
