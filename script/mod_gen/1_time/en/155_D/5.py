def func(N, K, A):
    A.sort()
    if A[0] >= 0:
        return A[K-1]
    elif A[N-1] <= 0:
        if (K % 2) == 0:
            return A[N-1]
        else:
            return A[N-2]
    else:
        left = 0
        right = N-1
        while True:
            mid = (left + right) // 2
            if A[mid] >= 0:
                right = mid
            else:
                left = mid
            if right - left == 1:
                break
        # print(left, right)
        if (K % 2) == 0:
            if A[left] * A[left+1] >= A[right-1] * A[right]:
                return A[left] * A[left+1]
            else:
                return A[right-1] * A[right]
        else:
            if A[left] * A[left+1] >= A[right-1] * A[right]:
                return A[right-1] * A[right]
            else:
                return A[left] * A[left+1]

if __name__ == '__main__':
    func()