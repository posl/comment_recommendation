def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        if x < A[0]:
            print(N)
        elif x > A[N-1]:
            print(0)
        else:
            # binary search
            left = 0
            right = N-1
            while left < right:
                mid = (left + right) // 2
                if A[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            print(N - left)

if __name__ == '__main__':
    main()