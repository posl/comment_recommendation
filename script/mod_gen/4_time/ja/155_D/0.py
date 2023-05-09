def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = -10**18
    r = 10**18
    while l+1<r:
        x = (l+r)//2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                l2 = -1
                r2 = N
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if A[i] * A[x2] < x:
                        r2 = x2
                    else:
                        l2 = x2
                cnt += N-r2
            else:
                l2 = -1
                r2 = N
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if A[i] * A[x2] < x:
                        l2 = x2
                    else:
                        r2 = x2
                cnt += r2
        cnt //= 2
        if cnt < K:
            l = x
        else:
            r = x
    print(l)

if __name__ == '__main__':
    main()