Synthesizing 10/10 solutions

=======
Suggestion 1

def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i
    ans = 0
    for i in range(n - 1):
        if b[i] > b[i + 1]:
            ans += 1
    print(ans + 1 if ans < n - 1 else -1)

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            print(-1)
            return
    ans = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            ans += 1
        else:
            ans += a[i]
    print(ans)
solve()

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        if a[i] > n:
            print(-1)
            exit()
        c[a[i] - 1] += 1
    ans = 0
    for i in range(n):
        if c[i] > i + 1:
            print(-1)
            exit()
        ans += i + 1 - c[i]
    print(ans)

solve()

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
        exit()
    ans = 0
    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            print(-1)
            exit()
        elif A[i + 1] - A[i] == 1:
            ans += 1
        else:
            ans += A[i]
    print(ans + A[-1])
solve()

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if a[0] != 1:
        print(-1)
        return
    for i in range(n-1):
        if a[i] + 1 < a[i+1]:
            print(-1)
            return
    ans = 0
    for i in range(n-1):
        if a[i] + 1 == a[i+1]:
            ans += 1
    print(n - 1 - ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        if A[0] == 1 or A[N - 1] == N:
            print(1)
        elif A[0] == N or A[N - 1] == 1:
            print(2)
        else:
            print(3)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == i + 1:
            ans += 1
    if ans == n:
        print(0)
    elif ans == n - 1:
        print(1)
    else:
        print(n - ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    B = [0 for i in range(N)]
    for i in range(N):
        B[A[i]-1] = i+1
    #print(B)
    ans = 0
    for i in range(N-1):
        if B[i] > B[i+1]:
            ans += 1
    print(ans+1)

=======
Suggestion 9

def solve():
    N = int(input())
    a = list(map(int, input().split()))

    if a[0] != 1:
        print(-1)
        return

    ans = 0
    for i in range(1, N):
        if a[i] == a[i - 1] + 1:
            ans += 1
        elif a[i] <= a[i - 1]:
            ans += a[i]
        else:
            print(-1)
            return
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    if ans == n:
        print(0)
    elif ans == n-1:
        print(1)
    else:
        print(n-ans)
