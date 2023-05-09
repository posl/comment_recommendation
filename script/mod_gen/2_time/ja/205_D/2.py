def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [1] + A + [10**18]
    #print(A)
    for k in K:
        #print(k)
        left = 0
        right = N + 1
        while right - left > 1:
            mid = (left + right) // 2
            #print("mid", mid)
            if A[mid] - A[mid - 1] <= k:
                k -= A[mid] - A[mid - 1]
                left = mid
                #print("left", left)
            else:
                right = mid
                #print("right", right)
        print(A[left] + k - 1)

if __name__ == '__main__':
    main()