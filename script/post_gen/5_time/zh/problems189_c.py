Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

=======
Suggestion 2

def solve(n, a):
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans = max(ans, x * (j - i + 1))
    return ans

=======
Suggestion 3

def solve(n, a):
    ans = 0
    for l in range(n):
        for r in range(l, n):
            x = a[l]
            for i in range(l, r+1):
                x = min(x, a[i])
            ans = max(ans, x*(r-l+1))
    return ans

=======
Suggestion 4

def solve():
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
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(1, a[j] + 1):
                if max < k * (j - i + 1):
                    max = k * (j - i + 1)
    print(max)
    return

=======
Suggestion 6

def solve(n, a):
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x*(r-l+1))
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j + 1])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 9

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
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for left in range(N):
        x = A[left]
        for right in range(left, N):
            x = min(x, A[right])
            ans = max(ans, x * (right - left + 1))
    print(ans)
