Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            return 0 if n == 1 else -1
        else:
            return -1
    if n == 1:
        return 0
    if d > 0:
        if x < a:
            return -1
        if x > a + (n - 1) * d:
            return -1
        if (x - a) % d == 0:
            return 0
        else:
            return 1
    else:
        if x > a:
            return -1
        if x < a + (n - 1) * d:
            return -1
        if (x - a) % d == 0:
            return 0
        else:
            return 1

print(solve())

=======
Suggestion 2

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
    else:
        if (X-A)%D == 0 and (X-A)//D >= 0:
            if N > (X-A)//D:
                print(N-(X-A)//D)
            else:
                print(0)
        else:
            print(-1)

=======
Suggestion 3

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a) % d == 0:
            if (x-a) // d >= 0:
                print((x-a) // d)
            else:
                print(1)
        else:
            print('inf')

=======
Suggestion 4

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if n == 1:
        return 0
    if x < a:
        if d < 0:
            return 1 + solve(x, a, -d, n)
        else:
            return 1 + solve(x, a, d, n)
    if x > a + (n - 1) * d:
        if d < 0:
            return 1 + solve(x, a, d, n)
        else:
            return 1 + solve(x, a, -d, n)
    if x == a:
        return 0
    if d < 0:
        return 1 + solve(x, a, -d, n)
    else:
        return min(1 + solve(x, a, -d, n), 1 + solve(x, a, d, n))

=======
Suggestion 5

def main():
    # input
    x, a, d, n = map(int, input().split())
    # compute
    ans = 0
    if d == 0:
        if x == a:
            ans = 0
        else:
            ans = 1
    else:
        if (x - a) % d == 0:
            ans = (x - a) // d
            if ans < 0:
                ans = -ans
        else:
            ans = 1
    # output
    print(ans)

=======
Suggestion 6

def solve():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if A == X:
            print(0)
        else:
            print(N)
        return
    if N == 1:
        if A == X:
            print(0)
        else:
            print(1)
        return
    if D > 0:
        if A > X:
            print(N)
            return
        if A + D * (N - 1) < X:
            print(N)
            return
        if (X - A) % D == 0:
            print(0)
            return
        else:
            print(1)
            return
    if D < 0:
        if A < X:
            print(N)
            return
        if A + D * (N - 1) > X:
            print(N)
            return
        if (X - A) % D == 0:
            print(0)
            return
        else:
            print(1)
            return

solve()

=======
Suggestion 7

def solve(x,a,d,n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    else:
        if abs(x-a) % abs(d) == 0:
            return abs(x-a) // abs(d)
        else:
            return -1

x,a,d,n = map(int,input().split())
print(solve(x,a,d,n))

=======
Suggestion 8

def solve(x, a, d, n):
    if a <= x <= a + d * (n - 1):
        return 0
    if x < a:
        return (a - x) // d + 1
    return (x - a) // d + 1

=======
Suggestion 9

def solve(x, a, d, n):
    if (x - a) % d != 0:
        return -1
    else:
        return (x - a) // d + 1

=======
Suggestion 10

def main():
    # Inputs
    X, A, D, N = map(int, input().split())
    # A + (N-1) * D = X
    # N = (X - A) / D + 1
    # N = (X - A + D) / D
    # N = X // D - A // D + 1
    # N = X // D - A // D + 1
    N = X // D - A // D + 1
    print(N)
