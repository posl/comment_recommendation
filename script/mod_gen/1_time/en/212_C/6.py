def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for i in range(N):
        j = bisect_left(B,A[i])
        if j==0:
            ans = min(ans,abs(A[i]-B[j]))
        elif j==M:
            ans = min(ans,abs(A[i]-B[j-1]))
        else:
            ans = min(ans,abs(A[i]-B[j-1]),abs(A[i]-B[j]))
    print(ans)

if __name__ == '__main__':
    main()