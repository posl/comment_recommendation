def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    left = 0
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < K:
            left = mid
        else:
            right = mid
    if A[left] < K:
        print(N - right)
    else:
        print(N - left)
