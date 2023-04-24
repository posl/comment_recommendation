Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 3

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
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        cnt = 0
        while r < n:
            while r < n and a[r] >= x:
                r += 1
            cnt += max(0, r-l)
            while l < r and a[l] < x:
                l += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            x = min(A[i:j])
            ans = max(ans, x*(j-i))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            ans += a[i-1]-a[i]
            a[i] = a[i-1]
    print(ans)
