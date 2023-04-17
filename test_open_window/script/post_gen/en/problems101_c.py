Synthesizing 10/10 solutions

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print((N-1+K-2)//(K-1))

main()

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i
    count = 0
    for i in range(N):
        if B[i] != i:
            count += 1
    print((count - 1) // (K - 1) + 1)

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + A[i - 1]
    ans = N
    for i in range(1, N - K + 2):
        tmp = dp[i + K - 1] - dp[i - 1]
        if tmp < ans:
            ans = tmp
    print(ans)

=======

def get_input():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, A

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    while max(A) > min(A) + K:
        ans += 1
        for i in range(N):
            if A[i] <= min(A) + K:
                A[i] = min(A) + K
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    while max(A) != min(A):
        ans += 1
        for i in range(0, N, K):
            A[i:i+K] = [min(A[i:i+K])]*K
    print(ans)

=======

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    B = [0]*N
    for i in range(N):
        B[A[i]] = i
    ans = 0
    for i in range(N):
        if A[i] != i:
            ans += 1
            j = B[i]
            A[i], A[j] = A[j], A[i]
            B[A[i]], B[A[j]] = B[A[j]], B[A[i]]
    print(ans//K)

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [int(s) for s in input().split()]
    #print(N, K)
    #print(A)
    A.sort(reverse=True)
    #print(A)
    ans = 0
    for i in range(N-K+1):
        ans += A[i]
    print(ans)

=======

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    #print(A)
    B = []
    for i in range(0, N, K):
        B.append(A[i:i+K])
    #print(B)
    ans = 0
    for b in B:
        ans += len(b)-1
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 1. How many operations are required to make all the elements equal?
    # 2. What is the minimum number of operations required?

    print(N - 1)
