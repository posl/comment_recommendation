def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    ans = []
    for k in K:
        left = 0
        right = N + 1
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] - A[mid - 1] - 1 < k:
                k -= A[mid] - A[mid - 1] - 1
                left = mid
            else:
                right = mid
        ans.append(A[left] + k)
    print('
'.join(map(str, ans)))
