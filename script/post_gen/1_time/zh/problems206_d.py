Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n // 2):
        ans += A[2 * i + 1] - A[2 * i]
    print(ans)
solve()

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == n - 1 - i:
            break
        if a[i] == a[i + 1]:
            ans += 1
            while i < n - 1 and a[i] == a[i + 1]:
                i += 1
        else:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i > 0 and a[i - 1] == a[i]:
            ans += 1
        elif i < n - 1 and a[i] == a[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A = [1, 5, 3, 2, 5, 2, 3, 1]
    # N = 8

    # A = [1, 2, 3, 4, 1, 2, 3]
    # N = 7

    # A = [200000]
    # N = 1

    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1

    # print(d)

    result = 0
    for i in d:
        if d[i] % 2 == 1:
            result += 1
    print(result)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = [0] + a + [0]
    ans = 0
    for i in range(1,n+2):
        if a[i-1] == a[i+1]:
            ans += 1
            a[i] = a[i-1]
    print(ans)

=======
Suggestion 6

def problem206_d():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n//2):
        ans += abs(a[i]-a[n-i-1])
    print(ans)
problem206_d()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            ans += 1
            a[i] = 0
            a[i + 1] = 0
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1:
        print(0)
        return

    A = sorted(A)

    cnt = 0
    prev = A[0]
    for i in range(1, N):
        if prev == A[i]:
            cnt += 1
            prev = -1
        else:
            prev = A[i]

    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == n-1:
            ans += 1
        elif a[i] == a[i+1]:
            ans += 1
        else:
            ans += 2
    print(ans//2)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 0
    j = N-1
    ans = 0
    while i < j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        elif A[i] < A[j]:
            i += 1
            A[i] += A[i-1]
            ans += 1
        else:
            j -= 1
            A[j] += A[j+1]
            ans += 1
    print(ans)
