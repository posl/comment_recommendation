def solve(N, K, A):
    A.sort()
    if A[0] >= 0:
        return A[K - 1]
    elif A[-1] <= 0:
        if K % 2 == 1:
            return A[-K]
        else:
            return A[K - 1]
    else:
        left = -1
        right = N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] >= 0:
                right = mid
            else:
                left = mid
        neg = right
        pos = N - neg
        if K <= neg * pos:
            left = -10 ** 18
            right = 10 ** 18
            while right - left > 1:
                mid = (left + right) // 2
                if check(N, K, A, mid):
                    right = mid
                else:
                    left = mid
            return right
        else:
            if K % 2 == 1:
                return A[-K // pos - 1]
            else:
                return A[K // neg - 1]
