Synthesizing 9/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K % 2 == 0:
            print(A[N-K])
        else:
            print(A[N-K-1])
        return
    #print(A)
    #pri

=======
Suggestion 3

def main():
    # input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))

    # compute
    As.sort()
    if As[0] >= 0:
        ans = As[K-1] * As[K-2]
    elif As[-1] <= 0:
        ans = As[-K] * As[-K-1]
    else:
        ans = As[-1] * As[-2]
        for i in range(K):
            if As[i] * As[i+1] > ans:
                break
            ans = As[i] * As[i+1]

    # output
    print(ans)

=======
Suggestion 4

def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    A = [0] + A

    def calc(x):
        cnt = 0
        for i in range(1, N + 1):
            if A[i] < 0:
                cnt += bisect_left(A, -(-x // A[i]), i + 1, N + 1) - (i + 1)
            else:
                cnt += N - bisect_left(A, x // A[i], i + 1, N + 1) + 1
        return cnt

    ng = -10 ** 18 - 1
    ok = 10 ** 18 + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if calc(mid) >= K:
            ok = mid
        else:
            ng = mid
    print(ok)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        m = (l + r) // 2
        if check(m, A, K):
            r = m
        else:
            l = m
    print(r)

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A = [abs(i) for i in A]
    A.sort()
    A = [0] + A

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(n, k)
    #print(A)
    #print(A[0])
    #print(A[n-1])
    #print(A[0]*A[n-1])
    #print(A[1])
    #print(A[n-2])
    #print(A[1]*A[n-2])
    #print(A[2])
    #print(A[n-3])
    #print(A[2]*A[n-3])
    #print(A[3])
    #print(A[n-4])
    #print(A[3]*A[n-4])
    #print(A[4])
    #print(A[n-5])
    #print(A[4]*A[n-5])
    #print(A[5])
    #print(A[n-6])
    #print(A[5]*A[n-6])
    #print(A[6])
    #print(A[n-7])
    #print(A[6]*A[n-7])
    #print(A[7])
    #print(A[n-8])
    #print(A[7]*A[n-8])
    #print(A[8])
    #print(A[n-9])
    #print(A[8]*A[n-9])
    #print(A[9])
    #print(A[n-10])
    #print(A[9]*A[n-10])
    #print(A[10])
    #print(A[n-11])
    #print(A[10]*A[n-11])
    #print(A[11])
    #print(A[n-12])
    #print(A[11]*A[n-12])
    #print(A[12])
    #print(A[n-13])
    #print(A[12]*A[n-13])
    #print(A[13])
    #print(A[n-14])
    #print(A[13]*A[n-14])
    #print(A[14])
    #print(A[n-15])
    #print(A[14]*A[n-15])
    #print(A[15])
    #print(A[n-16])
    #print(A[15]*A[n-16])
    #print(A[16])
    #print(A[n-17])
    #print(A[16]*
