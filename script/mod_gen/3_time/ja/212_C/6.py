def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for i in range(N):
        idx = bisect_left(B, A[i])
        if idx == M:
            ans = min(ans, abs(A[i]-B[idx-1]))
        elif idx == 0:
            ans = min(ans, abs(A[i]-B[idx]))
        else:
            ans = min(ans, abs(A[i]-B[idx]), abs(A[i]-B[idx-1]))
    print(ans)

if __name__ == '__main__':
    main()