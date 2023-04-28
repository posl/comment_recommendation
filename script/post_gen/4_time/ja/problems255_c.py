Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a) % d == 0:
            a1 = int((x-a) / d) + 1
            if a1 >= 1 and a1 <= n:
                print(0)
            else:
                print(1)
        else:
            a1 = int((x-a) / d) + 1
            if a1 >= 1 and a1 <= n:
                print(0)
            else:
                if a1 < 1:
                    a1 = 1
                if a1 > n:
                    a1 = n
                a2 = a + (a1-1) * d
                if abs(a2 - x) < abs(a2+d - x):
                    print(abs(a2 - x))
                else:
                    print(abs(a2+d - x))

=======
Suggestion 2

def solve(X,A,D,N):
    if D == 0:
        if X == A:
            return 0
        else:
            return -1
    if N == 1:
        if X == A:
            return 0
        else:
            return -1
    if N == 2:
        if X == A or X == A + D:
            return 0
        else:
            return -1
    if X == A:
        return 0
    if D < 0:
        D = -D
        X = -X
        A = -A
    if X < A:
        return -1
    if (X - A) % D != 0:
        return -1
    if (X - A) // D < N - 1:
        return -1
    return (X - A) // D - (N - 1)

=======
Suggestion 3

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if (x - a) % d == 0:
        if (x - a) // d < 0:
            print(1)
        else:
            print(0)
    else:
        if (x - a) // d < 0:
            print(2)
        else:
            print(1)

=======
Suggestion 4

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
    else:
        if (X-A)%D == 0 and (X-A)//D >= 0:
            print((X-A)//D)
        else:
            print(-1)

=======
Suggestion 5

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
            print(-1)

=======
Suggestion 6

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if (X-A)%D == 0 and (X-A)//D >= 0:
            print((X-A)//D)
        else:
            print(-1)

=======
Suggestion 7

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
    else:
        if ((X-A) % D == 0) and ((X-A) // D >= 0):
            print((X-A) // D)
        else:
            print(-1)

=======
Suggestion 8

def solve(x, a, d, n):
    if d == 0:
        return 0 if x == a else -1
    if (x - a) % d != 0:
        return -1
    return max(0, (x - a) // d + 1)

=======
Suggestion 9

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(0)
        return
    if X == A:
        print(0)
        return
    if X < A:
        if D > 0:
            print(-1)
            return
        else:
            if (A - X) % D == 0:
                print((A - X) // D)
            else:
                print(-1)
            return
    if X > A:
        if D < 0:
            print(-1)
            return
        else:
            if (X - A) % D == 0:
                print((X - A) // D)
            else:
                print(-1)
            return

=======
Suggestion 10

def count_operation(x, a, d, n):
    if d == 0:
        if x != a:
            return -1
        else:
            return 0
    else:
        if (x-a)%d != 0:
            return -1
        else:
            if (x-a)//d < 0:
                return -1
            else:
                if (x-a)//d < n:
                    return (x-a)//d
                else:
                    return -1
