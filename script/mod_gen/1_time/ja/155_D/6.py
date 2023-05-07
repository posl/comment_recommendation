def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = list(map(abs, A))
    if A[0] >= 0:
        print(A[K-1])
        exit()
    if A[N-1] <= 0:
        if K%2 == 0:
            print(-A[N-K])
        else:
            print(A[N-K])
        exit()
    if K <= N:
        print(A[K-1])
        exit()
    if K > ((N*(N-1))//2):
        print(A[N-1])
        exit()
    left = -1
    right = N
    while right - left > 1:
        mid = (left + right)//2
        if A[mid] < 0:
            left = mid
        else:
            right = mid
    neg = left + 1
    pos = N - neg
    if neg*pos >= K:
        left = -1
        right = N
        while right - left > 1:
            mid = (left + right)//2
            cnt = 0
            for i in range(neg):
                j = bisect.bisect_left(A, A[i]*A[mid]//A[neg-1])
                if j < neg:
                    cnt += neg - j
            for i in range(neg, N):
                j = bisect.bisect_left(A, A[i]*A[mid]//A[neg-1])
                if j >= neg:
                    cnt += j - neg
            if cnt >= K:
                right = mid
            else:
                left = mid
        print(A[right])
    else:
        left = -1
        right = N
        while right - left > 1:
            mid = (left + right)//2
            cnt = 0
            for i in range(neg):
                j = bisect.bisect_left(A, A[i]*A[mid]//A[N-1])
                if j < neg:
                    cnt += neg - j
            for i in range(neg, N):
                j = bisect.bisect_left(A, A[i]*A[mid]//A[N-1])
                if j >= neg:
                    cnt += j - neg
            if cnt >= K:

if __name__ == '__main__':
    main()