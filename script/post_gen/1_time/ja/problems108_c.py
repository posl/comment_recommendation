Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans = (N // K) ** 3 + (N // (K // 2) - N // K) ** 3
    else:
        ans = (N // K) ** 3
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int, input().split())
    ans = 0
    if k%2 == 0:
        ans = (n//k)**3 + ((n+k//2)//k)**3
    else:
        ans = (n//k)**3
    print(ans)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    ans = 0
    if K % 2 == 0:
        ans += (N//K)**3
        if N % K >= K//2:
            ans += ((N - N%K)//K + 1)**3
    else:
        ans += (N//K)**3
    print(ans)

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    ans = 0
    if k % 2 == 0:
        ans += ((n - k // 2) // k + 1) ** 3
        ans += ((n - k) // k + 1) ** 3
    else:
        ans += (n // k + 1) ** 3
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    ans = 0
    if k % 2 == 0:
        ans = pow(n//k,3)
        if n % k >= k//2:
            ans += pow(n//k+1,3)
    else:
        ans = pow(n//k,3)
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    if K % 2 == 0:
        K_ = K // 2
        print((N // K_) ** 3 + ((N + K_) // K_) ** 3)
    else:
        print((N // K) ** 3)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    ans = 0
    if K % 2 == 0:
        A = N // K
        ans += A ** 3
        if N >= K//2:
            B = (N - K//2) // K + 1
            ans += B ** 3
    else:
        A = N // K
        ans += A ** 3
    print(ans)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(n+1):
        tmp = k - i%k
        if tmp > n:
            continue
        else:
            ans += (n - tmp)//k + 1
    print(ans**3)

=======
Suggestion 10

def cal(N,K):
    if K%2 == 0:
        if N%2 == 0:
            return int(N*N*N/K)
        else:
            return int((N-1)*(N-1)*(N-1)/K)
    else:
        return int((N/K)**3)
N,K = map(int,input().split())
print(cal(N,K))
