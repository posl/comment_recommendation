def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (r + l) // 2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                cnt += N - bisect_left(A, (-mid - 1) // A[i])
            elif A[i] > 0:
                cnt += bisect_left(A, (mid - 1) // A[i])
            else:
                if mid > 0:
                    cnt += N
        cnt //= 2
        if cnt < K:
            l = mid
        else:
            r = mid
    print(r)

if __name__ == '__main__':
    main()