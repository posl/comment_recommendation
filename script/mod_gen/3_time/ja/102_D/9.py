def main():
    import sys
    from itertools import accumulate
    from bisect import bisect_right
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A = list(accumulate(A))
    res = 10**9
    for i in range(1, N-3):
        #print(A[i])
        j = bisect_right(A, A[i]//2, lo=i+1, hi=N-2)
        #print(j)
        if j <= N-2:
            res = min(res, abs(A[i]-A[j]*2))
        if j-1 >= i+1:
            res = min(res, abs(A[i]-A[j-1]*2))
        k = bisect_right(A, (A[i]+A[N-1])//2, lo=i+1, hi=N-2)
        #print(k)
        if k <= N-2:
            res = min(res, abs(A[N-1]-A[k]*2+A[i]))
        if k-1 >= i+1:
            res = min(res, abs(A[N-1]-A[k-1]*2+A[i]))
    print(res)

if __name__ == '__main__':
    main()