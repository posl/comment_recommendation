Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += max(0, A[i] - X * K)
        K = max(0, K - A[i] // X)
    print(ans)

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for a in A:
        if K > 0:
            if a > X:
                ans += X
                K -= 1
            else:
                ans += a
        else:
            ans += a
    print(ans)

=======
Suggestion 3

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] >= x:
            if k > 0:
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 4

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = [max(a - X * K, 0) for a in A]
    print(sum(B))

=======
Suggestion 5

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N - K:
            ans += max(A[i], 0)
        else:
            ans += max(A[i] - X, 0)
    print(ans)

=======
Suggestion 6

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(0, A[i] - X)
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N):
        if K > 0:
            K -= 1
            ans += A[i] - X
        else:
            ans += A[i]
    print(max(ans, 0))

=======
Suggestion 8

def main():
    n, k, x = map(int, input().split())
    ans = 0
    for i in range(n):
        a = int(input())
        if a > x:
            ans += a - x
        if k > 0:
            ans += min(a, x)
            k -= 1
        else:
            ans += a
    print(ans)

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, X)
    #print(A)
    A.sort()
    i = 0
    while i < N:
        if A[i] > X:
            break
        i += 1
    #print(i)
    if i <= K:
        print(sum(A[:i]))
    else:
        print(sum(A[:i-K]) + (i-K) * X)

main()

I am not good at English. I am sorry if my English is not good.

I am a Japanese student. I am interested in programming. I want to solve problems in programming contests.

I am not good at English. I am sorry if my English is not good.

I am a Japanese student. I am interested in programming. I want to solve problems in programming contests.

=======
Suggestion 10

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(sum([max(a - (i // K) * X, 0) for i, a in enumerate(A)]))
