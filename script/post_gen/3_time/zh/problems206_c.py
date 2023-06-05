Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if A[i] != A[j]:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += i - a.index(a[i])
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

solve()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[i] == a[j]:
            j += 1
        ans += (j - i - 1) * (j - i) // 2
        i = j
    print(ans)

=======
Suggestion 8

def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    return ans

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (10 ** 9 + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = n * (n - 1) // 2
    for i in range(10 ** 9 + 1):
        ans -= c[i] * (c[i] - 1) // 2
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)
