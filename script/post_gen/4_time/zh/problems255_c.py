Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
            return
        else:
            print(1)
            return
    if (X - A) % D != 0:
        print(-1)
        return
    else:
        if (X - A) // D < 0:
            print(-1)
            return
        else:
            if (X - A) // D + 1 > N:
                print(-1)
                return
            else:
                print(N - ((X - A) // D + 1))
                return

=======
Suggestion 3

def solve():
    # x,a,d,n=map(int,input().split())
    x,a,d,n=998244353,-10,-20,30
    if d==0:
        if x==a:
            print(0)
        else:
            print(1)
    elif n==1:
        if x==a:
            print(0)
        else:
            print(1)
    else:
        if d>0:
            if x<a or x>a+(n-1)*d:
                print(1)
            elif (x-a)%d==0:
                print(0)
            else:
                print(1)
        else:
            if x>a or x<a+(n-1)*d:
                print(1)
            elif (x-a)%d==0:
                print(0)
            else:
                print(1)

=======
Suggestion 4

def main():
    x, a, d, n = map(int, input().split())
    ans = 0
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    elif d > 0:
        while x < a:
            x += 1
            ans += 1
        while x > a + d * (n - 1):
            x -= 1
            ans += 1
        print(ans)
    else:
        while x > a:
            x -= 1
            ans += 1
        while x < a + d * (n - 1):
            x += 1
            ans += 1
        print(ans)

=======
Suggestion 5

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
    else:
        if (X - A) % D == 0 and (X - A) // D >= 0:
            print((X - A) // D)
        else:
            print(-1)

=======
Suggestion 6

def solve(x, a, d, n):
    if n == 1:
        return 0
    if x < a:
        return a - x
    elif x > a + (n - 1) * d:
        return x - (a + (n - 1) * d)
    else:
        return 0

x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))

=======
Suggestion 7

def get_input():
    return list(map(int, input().split()))

=======
Suggestion 8

def solve(x,a,d,n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    else:
        if (x - a) % d == 0 and (x - a) // d >= 0:
            return (x - a) // d
        else:
            return 1

=======
Suggestion 9

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if n == 1:
        if x == a:
            return 0
        else:
            return 1
    if n > 1:
        if (x - a) % d == 0:
            return 0
        else:
            return 1
