Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        A[0] = A[0] // 2
        A.sort()
    print(sum(A))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        a[0] = a[0] // 2
        a.sort()
    print(sum(a))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] // (2 ** min(i, M))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if M == 0:
            ans += A[i]
        else:
            if A[i] > 2 ** M:
                ans += A[i] - 2 ** M
                A[i] = 2 ** M
            M -= A[i].bit_length() - 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] <= m:
            m -= a[i]
        else:
            ans += a[i] - m
            m = 0
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [2, 13, 8]
    #N = 3
    #M = 3
    A.sort(reverse=True)
    #print(A)
    #print(N)
    #print(M)
    #print(A)

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] // (2 ** min(m, i))
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    ans = 0
    
    for i in range(n):
        ans += a[i] // 2**m
        m -= 1
        if m < 0:
            ans += a[i]
    
    print(ans)
    
main()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(N):
        ans -= A[i] // (2**M)
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A = [0] + A
    B = [0] * (N+1)
    for i in range(1, N+1):
        B[i] = B[i-1] + A[i]
    ans = 0
    for i in range(1, N+1):
        ans += A[i]
    for i in range(1, N+1):
        if A[i] == A[i-1]:
            continue
        else:
            if i-1 <= M:
                M -= (i-1)
                ans -= B[i-1]
            else:
                ans -= B[M]
                break
    print(ans)
