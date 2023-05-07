def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    zero = 0
    for i in range(N):
        if A[i] <= 0:
            zero += 1
        else:
            break
    if zero == 0:
        print(A[K-1])
    elif zero == N:
        print(A[-K])
    else:
        if K <= zero * (N-zero):
            l, r = 0, zero-1
            while l < r:
                m = (l+r+1)//2
                if A[m]*A[m+1] < 0:
                    r = m-1
                else:
                    l = m
            if K <= (l+1)*(zero-l-1):
                l, r = 0, l
                while l < r:
                    m = (l+r+1)//2
                    if A[m]*A[m+1] <= 0:
                        r = m-1
                    else:
                        l = m
                print(A[l]*A[l+1])
            else:
                K -= (l+1)*(zero-l-1)
                l, r = zero-1, zero
                while l < r:
                    m = (l+r+1)//2
                    if A[m]*A[m+1] <= 0:
                        r = m-1
                    else:
                        l = m
                print(A[l]*A[l+1])
        else:
            K -= zero * (N-zero)
            l, r = zero, N-1
            while l < r:
                m = (l+r+1)//2
                if A[m]*A[m+1] < 0:
                    l = m
                else:
                    r = m-1
            print(A[l]*A[l+1])

if __name__ == '__main__':
    main()