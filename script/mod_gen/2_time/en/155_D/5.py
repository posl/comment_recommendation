def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    if A[-1] <= 0:
        ans = A[-K]
    elif A[0] >= 0:
        ans = A[K-1]
    else:
        left = 0
        right = N-1
        while left <= right:
            mid = (left + right)//2
            if A[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        left = left - 1
        right = left + 1
        while K > 0:
            if left < 0:
                ans = A[right]
                right += 1
            elif right >= N:
                ans = A[left]
                left -= 1
            else:
                if A[left] * A[left-1] > A[right] * A[right+1]:
                    ans = A[left]
                    left -= 1
                else:
                    ans = A[right]
                    right += 1
            K -= 1
    print(ans)
main()

if __name__ == '__main__':
    main()