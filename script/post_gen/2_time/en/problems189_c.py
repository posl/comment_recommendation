Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, max(A)+1):
        l = 0
        r = 0
        while r < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            while r < N and A[r] < x:
                r += 1
            l = r
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, max(A)+1):
        cnt = 0
        for i in range(N):
            if A[i] >= x:
                cnt += 1
            else:
                ans = max(ans, cnt*x)
                cnt = 0
        ans = max(ans, cnt*x)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(ma

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for x in range(1, 10**5+1):
        tmp = 0
        for i in range(N):
            if A[i] >= x:
                tmp += 1
            else:
                ans = max(ans, tmp*x)
                tmp = 0
        ans = max(ans, tmp*x)
    print(ans)

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(0)
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for x in range(1, max(A)+1):
        cnt = 0
        for a in A:
            if a >= x:
                cnt += 1
            else:
                ans = max(ans, cnt*x)
                cnt = 0
        ans = max(ans, cnt*x)

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += a[i]*(n-i-1)
    print(ans + a[-1])
