Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    if n == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, n):
        if a[i] != a[i - 1] + 1:
            ans += 1
    print(ans)

=======
Suggestion 2

def problems148_d():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    if b[0] != 1:
        print(-1)
        return
    for i in range(1, n):
        if b[i] == 0:
            print(-1)
            return
    ans = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    a = [int(i) for i in input().split()]
    if a[0] != 1:
        print(-1)
        return
    for i in range(1, N):
        if a[i] - a[i-1] > 1:
            print(-1)
            return
    ans = N
    for i in range(N-1, -1, -1):
        if a[i] == ans:
            ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        print(N - ans + 1)

=======
Suggestion 5

def solve(N,a):
    ans = 0
    for i in range(1,N+1):
        if a[i] == i:
            ans += 1
    if ans == N:
        return 0
    else:
        return ans

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    c = 0
    for i in range(n):
        if b[i] != i+1:
            c += 1
    if c == 0:
        print(0)
    elif c == 2:
        print(1)
    else:
        print(-1)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            print(-1)
            return
        elif A[i+1] - A[i] == 1:
            ans += 1
        else:
            ans += A[i+1]
    print(ans)

solve()

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        ans = 0
        for i in range(N):
            if a[i] != i + 1:
                ans += 1
        print(ans)

=======
Suggestion 10

def solve(N, A):
    # N = int(input())
    # A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        return 0
    elif ans == N - 1:
        return 1
    else:
        return N - ans
