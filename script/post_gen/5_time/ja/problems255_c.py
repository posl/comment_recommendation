Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(x,a,d,n):
    if d==0:
        if x==a:
            return 0
        else:
            return -1
    else:
        if (x-a)%d==0:
            k=(x-a)//d
            if k>=0 and k<=n-1:
                return k
            else:
                return -1
        else:
            return -1

=======
Suggestion 2

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    if (x - a) % d != 0:
        return -1
    ans = 0
    if (x - a) // d > 0:
        ans += (x - a) // d
        x -= (x - a) // d * d
    else:
        ans += -((x - a) // d)
        x -= -((x - a) // d) * d
    if x != a:
        ans += 1
        x -= d
    if x != a:
        ans += 1
    return ans

x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))

=======
Suggestion 3

def solve():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
        return
    if N == 1:
        if X == A:
            print(0)
        else:
            print(-1)
        return
    if (X-A)%D != 0:
        print(-1)
        return
    n = (X-A)//D + 1
    if n < 1:
        print(-1)
        return
    if n > N:
        print(-1)
        return
    print(N-n)
    return

=======
Suggestion 4

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if d > 0:
        if x < a:
            print(1)
        else:
            print((x - a) // d + 1)
        return
    if d < 0:
        if x > a:
            print(1)
        else:
            print((a - x) // (-d) + 1)
        return
    print(0)
    return

=======
Suggestion 5

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if (X - A) % D == 0 and (X - A) // D >= 0:
            print((X - A) // D)
        else:
            print(1 + (X - A) // D + 1)

=======
Suggestion 6

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print("inf")
    else:
        if (x-a)%d == 0:
            if (x-a)//d >= 0:
                print((x-a)//d+1)
            else:
                print("inf")
        else:
            print("inf")

=======
Suggestion 7

def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x < a:
            print(a-x)
        else:
            print(x-a)
    else:
        if n % 2 == 0:
            if x < a:
                print(a-x)
            else:
                print(x-a)
        else:
            if x < a:
                if (a-x) % d == 0:
                    print((a-x)//d)
                else:
                    print((a-x)//d + 1)
            else:
                if (x-a) % d == 0:
                    print((x-a)//d)
                else:
                    print((x-a)//d + 1)

=======
Suggestion 8

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if (X-A) % D == 0 and (X-A) / D >= 0:
            print(int((X-A)/D))
        else:
            print(-1)

=======
Suggestion 9

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if A == X:
            print(0)
        else:
            print(-1)
    elif N == 1:
        if (X - A) % D == 0:
            print((X - A) // D)
        else:
            print(-1)
    else:
        if (X - A) % D == 0 and (X - A) // D >= 0:
            print((X - A) // D)
        else:
            print(-1)

=======
Suggestion 10

def get_input():
    x,a,d,n = input().split()
    x = int(x)
    a = int(a)
    d = int(d)
    n = int(n)
    return x,a,d,n
