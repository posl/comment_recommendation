def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print('No')
        return
    A.sort()
    B.sort()
    A = A[::-1]
    B = B[::-1]
    for i in range(N):
        if A[i] > B[i]:
            print('No')
            return
    # 二分探索
    left = 0
    right = 10**18
    while left + 1 < right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(N):
            cnt += bisect_right(B, mid + A[i])
        if cnt >= N:
            right = mid
        else:
            left = mid
    print('Yes')
