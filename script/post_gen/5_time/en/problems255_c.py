Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    if n == 1:
        if x == a:
            return 0
        else:
            return -1
    if (x - a) % d != 0:
        return -1
    ans = 0
    if d > 0:
        if x < a:
            ans += (a - x) // d
            x += ans * d
        if x > a:
            ans += (x - a) // d
            x -= ans * d
        if x != a:
            return -1
        if ans >= n:
            return -1
        ans += (n - ans) // 2
    else:
        if x > a:
            ans += (x - a) // d
            x += ans * d
        if x < a:
            ans += (a - x) // d
            x -= ans * d
        if x != a:
            return -1
        if ans >= n:
            return -1
        ans += (n - ans) // 2
    return ans

x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))

=======
Suggestion 2

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if A == X:
            print(0)
        else:
            print("inf")
        return
    if D > 0:
        if X < A or X > A + D * (N - 1):
            print(0)
            return
        if (X - A) % D == 0:
            print((X - A) // D)
        else:
            print("inf")
        return
    if D < 0:
        if X > A or X < A + D * (N - 1):
            print(0)
            return
        if (X - A) % D == 0:
            print((X - A) // D)
        else:
            print("inf")
        return

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
        if (x-a)%d == 0 and (x-a)//d >= 0:
            print((x-a)//d)
        else:
            print(1+min(abs(x-a)%d,abs(x-a+d)%d))

=======
Suggestion 4

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if D > 0:
            if X < A:
                print(1)
            elif X == A:
                print(0)
            else:
                if (X-A)%D == 0:
                    print((X-A)//D)
                else:
                    print((X-A)//D+1)
        else:
            if X > A:
                print(1)
            elif X == A:
                print(0)
            else:
                if (X-A)%D == 0:
                    print((X-A)//D)
                else:
                    print((X-A)//D+1)

=======
Suggestion 5

def solve():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            return 0
        else:
            return N
    else:
        if (X - A) % D == 0 and (X - A) // D >= 0:
            return min((X - A) // D, N)
        else:
            return N

print(solve())

=======
Suggestion 6

def solve():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            return 0
        else:
            return 1

    if N == 1:
        if A == X:
            return 0
        else:
            return 1

    if D > 0:
        if X <= A:
            return 1
        else:
            return 1 + (X - A) // D
    else:
        if X >= A:
            return 1
        else:
            return 1 + (A - X) // (-D)

print(solve())

=======
Suggestion 7

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        return abs(x-a)
    if n == 1:
        return min(abs(x-a), abs(x-(a+d)))
    if x < a:
        return abs(x-a)
    if x > a + d * (n-1):
        return abs(x-(a+d*(n-1)))
    if (x-a) % d == 0:
        return 0
    else:
        return min(abs(x-(a+d*((x-a)//d))), abs(x-(a+d*((x-a)//d+1))))

=======
Suggestion 8

def solution(x, a, d, n):
    if n == 1:
        return 0
    elif d == 0:
        return abs(x - a)
    else:
        if n % 2 == 0:
            return abs(x - a - (n // 2) * d)
        else:
            return min(abs(x - a - (n // 2) * d), abs(x - a - (n // 2 - 1) * d - d))

=======
Suggestion 9

def solve(x,a,d,n):
    if a <= x <= a + (n-1)*d:
        return 0
    elif a > x:
        return -1
    else:
        return 1 + solve(x+d,a,d,n)

x,a,d,n = map(int,input().split())
print(solve(x,a,d,n))

=======
Suggestion 10

def solve(x, a, d, n):
    return 0
