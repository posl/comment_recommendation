Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j])**2
    print(ans)

=======
Suggestion 5

def solve(N, A):
    ans = 0
    for i in range(1, N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    return ans

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (n - 1) * a[i] ** 2
    for i in range(n - 1):
        ans -= 2 * a[i] * sum(a[i + 1:])
    print(ans)

main()

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)
