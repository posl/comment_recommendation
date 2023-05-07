def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] <= 0:
        print(A[-K])
    elif A[0] >= 0:
        print(A[K-1])
    else:
        ans = 0
        i = 0
        j = N-1
        while i < j:
            if A[i]*A[i+1] > A[j]*A[j-1]:
                ans = A[i]*A[i+1]
                i += 2
            else:
                ans = A[j]*A[j-1]
                j -= 2
            K -= 1
            if K == 0:
                print(ans)
                return
        print(A[i]*A[j])

if __name__ == '__main__':
    main()