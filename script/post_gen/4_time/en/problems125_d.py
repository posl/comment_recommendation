Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(sum(A) - 2 * A[0])
    elif A[-1] <= 0:
        print(-sum(A) + 2 * A[-1])
    else:
        print(sum(map(abs, A)))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - 2 * min(abs(a[0]), abs(a[-1])))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0:
        if N % 2 == 0:
            print(sum(map(abs, A)))
        else:
            print(sum(map(abs, A)) - 2 * min(map(abs, A)))
    else:
        print(sum(A))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0 and A[-1] < 0:
        if N % 2 == 0:
            print(-sum(A))
        else:
            print(-sum(A) + 2 * A[0])
    elif A[0] < 0 and A[-1] >= 0:
        print(-sum(A))
    else:
        print(sum(A))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [abs(a[i]) for i in range(n)]
    c = [a[i] for i in range(n) if a[i] < 0]
    if len(c) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = 0
    p = 0
    for i in range(N):
        if A[i] < 0:
            m += 1
            A[i] = -A[i]
        p += A[i]
    if m % 2 == 0:
        print(p)
    else:
        print(p - 2 * min(A))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - 2 * a[0])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    s = sum(A)
    if s < 0:
        print(s + 2 * A[0])
    elif s == 0:
        print(2 * A[0])
    else:
        print(s - 2 * A[0])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    minus = 0
    min_abs = 10**9
    sum = 0
    for i in range(N):
        if A[i] < 0:
            minus += 1
        sum += abs(A[i])
        min_abs = min(min_abs, abs(A[i]))
    if minus % 2 == 0:
        print(sum)
    else:
        print(sum - min_abs * 2)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    if A[0] < 0:
        for i in range(N):
            ans += -A[i]
    else:
        for i in range(N):
            ans += A[i]
        if A[0] == 0:
            pass
        elif A[0] > 0:
            ans -= 2*A[0]
        else:
            ans += 2*A[0]
    print(ans)
main()
