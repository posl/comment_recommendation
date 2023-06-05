Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N = int(input())
    A = list(map(int,input().split()))
    return N,A

=======
Suggestion 2

def get_average(a):
    return sum(a)/len(a)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(a[i:j]) % (j-i) == 0:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(1, 2**N):
        s = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j]
        if s % 2 == 0:
            ans += 1
    print(ans)
    return

=======
Suggestion 5

def problems262_d():
    return None

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    mod = 998244353
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] == A[j]:
                ans += 1
                ans %= mod
            elif (A[i]+A[j])%2 == 0:
                mid = (A[i]+A[j])//2
                if mid in A:
                    ans += 1
                    ans %= mod
    print(ans)
main()

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * (2**(N - 1))
    print(ans % 998244353)
solve()

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 2**N):
        sum = 0
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                sum += A[j]
                cnt += 1
        if sum % cnt == 0:
            ans += 1
    print(ans)

solve()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) % (j-i+1) == 0:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1 << n):
        sum = 0
        cnt = 0
        for j in range(n):
            if i & 1 << j:
                sum += a[j]
                cnt += 1
        if sum % cnt == 0:
            ans += 1
    print(ans)
