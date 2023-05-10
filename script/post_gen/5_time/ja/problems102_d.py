Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = [0]
    for i in range(n):
        p.append(p[i]+a[i])
    ans = 10**9
    for i in range(1,n-2):
        l = p[i]
        r = p[-1]-p[i]
        ans = min(ans,abs(l-r))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 10 ** 9
    t = 0
    for i in range(n - 1):
        t += a[i]
        ans = min(ans, abs(s - 2 * t))
    print(ans)
main()

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A_acc = [0]
    for i in range(N):
        A_acc.append(A_acc[i]+A[i])
    #print(A_acc)
    ans = 10**9
    for i in range(1,N-2):
        for j in range(i+1,N-1):
            #print(i,j)
            P = A_acc[i]
            Q = A_acc[j]-A_acc[i]
            R = A_acc[N]-A_acc[j]
            S = A_acc[N]-A_acc[j]
            #print(P,Q,R,S)
            tmp = max(P,Q,R,S)-min(P,Q,R,S)
            if tmp < ans:
                ans = tmp
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float("inf")
    left = 0
    right = s
    for i in range(n-1):
        left += a[i]
        right -= a[i]
        ans = min(ans, abs(left-right))
    print(ans)
    return 0

=======
Suggestion 5

def main():
    N=int(input())
    A=list(map(int,input().split()))
    for i in range(1,N):
        A[i]+=A[i-1]
    ans=10**9
    for i in range(N-3):
        ans=min(ans,abs(A[i]-2*A[i+1]+A[-1]))
    print(ans)
main()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    s1 = 0
    s2 = 0
    ans = 10**10
    for i in range(n-1):
        s1 += a[i]
        s2 = s - s1
        ans = min(ans, abs(s1-s2))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    P = 0
    Q = 0
    R = 0
    S = 0
    min_diff = 10**9

    for i in range(1, N-2):
        P += A[i-1]
        Q = 0
        for j in range(i+1, N-1):
            Q += A[j-1]
            R = 0
            for k in range(j+1, N):
                R += A[k-1]
                S = A_sum - P - Q - R
                max_val = max(P, Q, R, S)
                min_val = min(P, Q, R, S)
                min_diff = min(min_diff, max_val - min_val)
    print(min_diff)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    D = [0] * (N + 1)
    E = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
        C[i + 1] = C[i] + A[i]
        D[i + 1] = D[i] + A[i]
        E[i + 1] = E[i] + A[i]
    for i in range(N):
        B[i + 1] = max(B[i + 1], B[i])
    for i in range(N):
        C[i + 1] = min(C[i + 1], C[i])
    for i in range(N):
        D[i + 1] = max(D[i + 1], D[i])
    for i in range(N):
        E[i + 1] = min(E[i + 1], E[i])
    ans = 10 ** 18
    for i in range(1, N - 1):
        ans = min(ans, abs(B[i] - C[i]) + abs(D[i] - E[i + 1]))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    x = 0
    for i in range(n):
        x += a[i]
        if x >= s/2:
            break
    y = x - a[i]
    print(min(abs(x-y), abs(s-x-(s-y))))

=======
Suggestion 10

def main():
    #n = int(input())
    #a = [int(x) for x in input().split()]
    n = 10
    a = [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]
    #n = 7
    #a = [1, 2, 3, 1000000000, 4, 5, 6]
    #n = 5
    #a = [3, 2, 4, 1, 2]
    #n = 4
    #a = [1, 1, 1, 1]
    #n = 4
    #a = [1, 2, 3, 4]
    #n = 4
    #a = [1, 2, 3, 3]
    #n = 4
    #a = [1, 2, 2, 3]
    #n = 4
    #a = [1, 1, 2, 2]
    #n = 4
    #a = [1, 2, 1, 2]
    #n = 4
    #a = [1, 1, 1, 2]
    #n = 4
    #a = [1, 1, 2, 1]
    #n = 4
    #a = [1, 2, 1, 1]
    #n = 4
    #a = [2, 1, 1, 1]
    #n = 4
    #a = [1, 1, 1, 1]
    #n = 4
    #a = [2, 2, 2, 2]
    #n = 4
    #a = [3, 3, 3, 3]
    #n = 4
    #a = [4, 4, 4, 4]
    #n = 4
    #a = [5, 5, 5, 5]
    #n = 4
    #a = [6, 6, 6, 6]
    #n = 4
