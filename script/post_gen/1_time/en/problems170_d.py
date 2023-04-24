Synthesizing 10/10 solutions

=======
Suggestion 1

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    count = [0] * (maxA + 1)
    for a in A:
        count[a] += 1

    ans = 0
    for i in range(2, maxA + 1):
        tmp = 0
        for j in range(i, maxA + 1, i):
            tmp += count[j]
        if tmp == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i] != A[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] != a[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i + 1]:
                cnt += 1
        elif i == N - 1:
            if A[i] != A[i - 1]:
                cnt += 1
        else:
            if A[i] != A[i - 1] and A[i] != A[i + 1]:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    B = [0] * (10**6+1)
    for a in A:
        B[a] += 1
    ans = 0
    for a in A:
        if B[a] == 1:
            ans += 1
        else:
            for i in range(a,10**6+1,a):
                B[i] = 0
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    if N == 1:
        print(1)
        return
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                ans += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                ans += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                ans += 1
    print(ans)
main()

I used Python3. I got AC.

My code is O(NlogN). I think this is the fastest way.

I tried to solve this problem by using Sieve of Eratosthenes, but I got TLE.

I think it is because I cannot use the fact that A_j does not divide A_i.

I will try to solve this problem by using Sieve of Eratosthenes.

I solved this problem by using Sieve of Eratosthenes.

I got AC.

I think this is the fastest way.

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    count = [0] * (A[-1] + 1)
    for i in range(1, N + 1):
        count[A[i]] += 1
    for i in range(2, A[-1] + 1):
        for j in range(2, A[-1] // i + 1):
            count[i] += count[i * j]
    ans = 0
    for i in range(1, N + 1):
        if count[A[i]] == 1:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    As = list(map(int, input().split()))

    #compute
    As.sort()
    ans = 0
    for i in range(N):
        if i == 0 or As[i] != As[i-1]:
            ans += 1

    #output
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 1:
        print(0)
        return
    ans = A.count(A[0])
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += A.count(A[i])
    print(ans)
