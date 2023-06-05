def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (r + l) // 2
        count = 0
        for i in range(N):
            if A[i] < 0:
                l2 = -1
                r2 = N
                while r2 - l2 > 1:
                    mid2 = (r2 + l2) // 2
                    if A[i] * A[mid2] < mid:
                        r2 = mid2
                    else:
                        l2 = mid2
                count += N - r2
            else:
                l2 = -1
                r2 = N
                while r2 - l2 > 1:
                    mid2 = (r2 + l2) // 2
                    if A[i] * A[mid2] < mid:
                        l2 = mid2
                    else:
                        r2 = mid2
                count += r2
            if A[i] * A[i] < mid:
                count -= 1
        if count < K:
            l = mid
        else:
            r = mid
    print(l)

if __name__ == '__main__':
    main()