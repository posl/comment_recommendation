Synthesizing 9/10 solutions

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
            ans = max(ans, x*(j-i+1))
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

def solve():
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
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, x * (j-i+1))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 100001):
        l = 0
        r = 0
        while l < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            l += 1
            if r < l:
                r = l
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5 + 1):
        l = 0
        r = 0
        while r < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, (r - l) * x)
            while r < N and A[r] < x:
                r += 1
            l = r
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10 ** 5 + 1):
        l = 0
        for r in range(N):
            while l <= r and A[l] < x:
                l += 1
            if l <= r:
                ans = max(ans, (r - l + 1) * x)
    print(ans)
main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        left = 0
        right = 0
        while left < N:
            while right < N and A[right] >= x:
                right += 1
            ans = max(ans, x*(right-left))
            left = right
            while left < N and A[left] < x:
                left += 1
            right = left
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        for j in range(i+1,N+1):
            for k in range(1,10**5+1):
                if min(A[i:j]) >= k:
                    ans = max(ans,k*(j-i))
    print(ans)
