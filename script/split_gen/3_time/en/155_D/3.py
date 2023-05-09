def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    if A[0] >= 0:
        ans = A[K-1]
    else:
        if A[N-1] <= 0:
            if K % 2 == 0:
                ans = A[N-1]
            else:
                ans = A[0]
        else:
            if K % 2 == 0:
                if abs(A[0]) > A[N-1]:
                    ans = A[0]
                else:
                    ans = A[N-1]
            else:
                ans = A[K-1]
    print(ans)
main()
