Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                p = sum(a[:i])
                q = sum(a[i:j])
                r = sum(a[j:k])
                s = sum(a[k:])
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        left[i + 1] = left[i] + A[i]
        right[i + 1] = right[i] + A[N - 1 - i]
    left_max = [0] * (N + 1)
    right_max = [0] * (N + 1)
    for i in range(N):
        left_max[i + 1] = max(left_max[i], left[i + 1])
        right_max[i + 1] = max(right_max[i], right[i + 1])
    ans = 10 ** 18
    for i in range(N + 1):
        ans = min(ans, max(left_max[i], right_max[N - i]) - min(left[i], right[N - i]))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    ans = float("inf")
    j = 1
    for i in range(2, N - 1):
        while B[i] - B[j] >= B[j]:
            j += 1
        ans = min(ans, max(B[j], B[i] - B[j]) - min(B[j], B[i] - B[j]))
        ans = min(ans, max(B[N] - B[i], B[i] - B[j]) - min(B[N] - B[i], B[i] - B[j]))
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = float("inf")
    for i in range(2, n-1):
        for j in range(i+1, n):
            p = s[i]
            q = s[j] - s[i]
            r = s[n] - s[j]
            max_ = max(p, q, r)
            min_ = min(p, q, r)
            ans = min(ans, max_ - min_)
    print(ans)

solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, N):
        for j in range(i+1, N):
            P = sum(A[:i])
            Q = sum(A[i:j])
            R = sum(A[j:j+1])
            S = sum(A[j+1:])
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    B = [0] * (N + 2)
    C = [0] * (N + 2)
    D = [0] * (N + 2)
    E = [0] * (N + 2)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i]
    for i in range(1, N + 1):
        C[i] = C[i - 1] + A[i] * (-1) ** i
    for i in range(1, N + 1):
        D[i] = D[i - 1] + A[i] * (-1) ** (i + 1)
    for i in range(1, N + 1):
        E[i] = E[i - 1] + A[i] * (-1) ** i
    B.sort()
    C.sort()
    D.sort()
    E.sort()
    print(max(B[-1] - B[1], B[-2] - B[0], C[-1] - C[1], C[-2] - C[0], D[-1] - D[1], D[-2] - D[0], E[-1] - E[1], E[-2] - E[0]))

=======
Suggestion 7

def main():
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    ans=10**9
    t=0
    for i in range(n-1):
        t+=a[i]
        if t*2==s:
            ans=0
            break
        elif t*2>s:
            ans=min(ans,abs(t*2-s))
            ans=min(ans,abs(t*2-s+a[i+1]*2))
            break
        else:
            ans=min(ans,abs(t*2-s))
            ans=min(ans,abs(t*2-s+a[i+1]*2))
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = S
    s = 0
    for i in range(N-1):
        s += A[i]
        ans = min(ans, abs(S - s - s))
    print(ans)

=======
Suggestion 9

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a_sum=[0]
    for i in range(n):
        a_sum.append(a_sum[i]+a[i])
    ans=10**9
    for i in range(1,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                p=a_sum[i]
                q=a_sum[j]-a_sum[i]
                r=a_sum[k]-a_sum[j]
                s=a_sum[n]-a_sum[k]
                max_num=max(p,q,r,s)
                min_num=min(p,q,r,s)
                ans=min(ans,max_num-min_num)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0 for i in range(N)]
    C = [0 for i in range(N)]
    D = [0 for i in range(N)]
    E = [0 for i in range(N)]
    B[0] = A[0]
    C[0] = A[1]
    D[0] = A[2]
    E[0] = A[3] + A[4]
    for i in range(1, N):
        B[i] = B[i-1] + A[i]
        if i >= 2:
            C[i] = C[i-1] + A[i]
        if i >= 3:
            D[i] = D[i-1] + A[i]
        if i >= 4:
            E[i] = E[i-1] + A[i]
    #print(B)
    #print(C)
    #print(D)
    #print(E)
    ans = 10**9
    for i in range(1, N-2):
        #print(i)
        for j in range(i+1, N-1):
            #print(j)
            for k in range(j+1, N):
                #print(k)
                p = B[i-1]
                q = C[j-1] - C[i-1]
                r = D[k-1] - D[j-1]
                s = E[N-1] - E[k-1]
                #print(p, q, r, s)
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
