Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = s
    t = 0
    for i in range(n - 1):
        t += a[i]
        ans = min(ans, abs(s - t - t))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = [0] * (N + 1)
    A_sum[0] = 0
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    #print(A_sum)
    min_diff = 10 ** 9
    for i in range(2, N - 1):
        for j in range(1, i):
            P = A_sum[j]
            Q = A_sum[i] - A_sum[j]
            for k in range(i + 1, N):
                R = A_sum[k] - A_sum[i]
                S = A_sum[N] - A_sum[k]
                max_num = max(P, Q, R, S)
                min_num = min(P, Q, R, S)
                min_diff = min(min_diff, max_num - min_num)
    print(min_diff)

=======
Suggestion 3

def get_min_max_diff(A):
    N = len(A)
    min_diff = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                P = sum(A[:i])
                Q = sum(A[i:j])
                R = sum(A[j:k])
                S = sum(A[k:])
                diff = max(P, Q, R, S) - min(P, Q, R, S)
                if diff < min_diff:
                    min_diff = diff
    return min_diff

=======
Suggestion 4

def solve(n, a):
    a = [0] + a + [0]
    for i in range(n):
        a[i + 1] += a[i]
    ans = 10 ** 9
    l = 0
    r = 3
    for i in range(1, n - 2):
        while l < i - 1 and abs(a[l] - a[i] - a[i]) >= abs(a[l + 1] - a[i] - a[i]):
            l += 1
        while r < n - 1 and abs(a[r] - a[n] - a[n] + a[i]) >= abs(a[r + 1] - a[n] - a[n] + a[i]):
            r += 1
        ans = min(ans, max(abs(a[l] - a[i] - a[i]), abs(a[r] - a[n] - a[n] + a[i])))
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    ans = 10**9
    for i in range(1,n-2):
        l = 0
        r = i
        while l+1<r:
            m = (l+r)//2
            if s[m]<=s[i+1]-s[m]:
                l = m
            else:
                r = m
        p = s[l]
        q = s[i+1]-s[l]
        l = i+1
        r = n
        while l+1<r:
            m = (l+r)//2
            if s[m]-s[i+1]<=s[n]-s[m]:
                l = m
            else:
                r = m
        r = l
        l = i+1
        while l+1<r:
            m = (l+r)//2
            if s[m]-s[i+1]<=s[n]-s[m]:
                l = m
            else:
                r = m
        r = l
        s = s[n]-s[r]
        r = s[i+1]-s[l]
        ans = min(ans,max(p,q,r,s)-min(p,q,r,s))
        ans = min(ans,max(p,q,s-r,s)-min(p,q,s-r,s))
        ans = min(ans,max(p,r,s-q,s)-min(p,r,s-q,s))
        ans = min(ans,max(q,r,s-p,s)-min(q,r,s-p,s))
        ans = min(ans,max(p,s-q-r,s)-min(p,s-q-r,s))
        ans = min(ans,max(q,s-p-r,s)-min(q,s-p-r,s))
        ans = min(ans,max(r,s-p-q,s)-min(r,s-p-q,s))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 前から累積和
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]

    # 二分探索
    ans = float('inf')
    for i in range(2, N - 1):
        # B[i]がPの累積和
        # B[N] - B[i]がQ,R,Sの累積和
        # 二分探索でPを探索
        # 二分探索でQ,R,Sの中で最大と最小を探索
        # 二分探索でP,Q,R,Sの中で最大と最小を探索
        p = B[i] // 2
        l = 0
        r = i
        while r - l > 1:
            m = (l + r) // 2
            if B[i] - B[m] >= p:
                l = m
            else:
                r = m
        q = B[l]
        r = B[i] - q
        s = B[N] - B[i]
        ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
        p = B[N] // 2
        l = i
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if B[m] - B[i] >= p:
                r = m
            else:
                l = m
        q = B[i] - B[l]
        r = B[N] - B[m]
        s = B[N] - B[i]
        ans = min(ans, max(p, q, r, s) - min(p, q, r, s))

    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    #print(A)
    S = sum(A)
    #print(S)
    min_diff = S
    for i in range(1, N):
        #print(i)
        for j in range(i+1, N):
            #print(j)
            for k in range(j+1, N):
                #print(k)
                P = sum(A[0:i])
                Q = sum(A[i:j])
                R = sum(A[j:k])
                S = sum(A[k:])
                #print(P, Q, R, S)
                min_diff = min(min_diff, max(P, Q, R, S) - min(P, Q, R, S))
    print(min_diff)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i]+A[i]
    C = [0]*(N+1)
    for i in range(N):
        C[i+1] = C[i]+A[i]
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = D[i]+A[i]
    E = [0]*(N+1)
    for i in range(N):
        E[i+1] = E[i]+A[i]
    for i in range(1,N+1):
        C[i] = max(C[i], C[i-1])
    for i in range(N-1,-1,-1):
        D[i] = min(D[i], D[i+1])
    ans = 10**18
    j = N
    for i in range(N+1):
        while j > 0 and B[i] + D[j] < B[N]//2:
            j -= 1
        if j > 0:
            ans = min(ans, max(B[i], B[N]-B[i]) - max(C[i], D[j]))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    ans = s
    p = 0
    q = 0
    for i in range(1,n):
        p += a[i-1]
        q += a[i-1]
        r = s-p
        s = r
        ans = min(ans,abs(max(p,q,r,s)-min(p,q,r,s)))
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print("N:", N, "A:", A)
    #A = [3,2,4,1,2]
    #A = [10,71,84,33,6,47,23,25,52,64]
    #A = [1,2,3,1000000000,4,5,6]
    #N = 7
    #N = 10
    #N = 5
    #print("N:", N, "A:", A)
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    D = [0] * (N + 1)
    E = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
    for i in range(1, N + 1):
        C[i] = C[i - 1] + A[i - 1]
    for i in range(1, N + 1):
        D[i] = D[i - 1] + A[i - 1]
    for i in range(1, N + 1):
        E[i] = E[i - 1] + A[i - 1]
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
