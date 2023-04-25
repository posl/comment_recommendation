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
        if n == 1:
            print(abs(x-a))
        else:
            diff = x - a
            if diff % d == 0:
                print(0)
            else:
                print(1)

=======
Suggestion 2

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if n == 1:
            if x == a:
                print(0)
            else:
                print(1)
        else:
            if x == a:
                print(0)
            else:
                if d > 0:
                    if a < x and x < a + d * n:
                        print(1)
                    else:
                        print(2)
                else:
                    if a + d * n < x and x < a:
                        print(1)
                    else:
                        print(2)

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

    if a > x:
        if d > 0:
            print(1)
        else:
            print(2)
        return

    if d < 0:
        if a + d * (n - 1) < x:
            print(1)
        else:
            print(2)
        return

    if a + d * (n - 1) < x:
        print(1)
    else:
        print(2)

=======
Suggestion 4

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    else:
        if x == a:
            return 0
        else:
            if (x - a) % d == 0:
                return abs((x - a) // d)
            else:
                return abs((x - a) // d) + 1

=======
Suggestion 5

def solve():
    X, A, D, N = map(int, input().split())
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
        if X == A:
            return 0
        elif X == A + D or X == A - D:
            return 1
        else:
            return -1

    if N % 2 == 0:
        if X % 2 == 0:
            if X % D == 0:
                return 1
            else:
                return 2
        else:
            if (X + D) % D == 0:
                return 2
            else:
                return 3
    else:
        if X % 2 == 0:
            if (X + D) % D == 0:
                return 2
            else:
                return 3
        else:
            if X % D == 0:
                return 1
            else:
                return 2

=======
Suggestion 6

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if d > 0:
        if a > x:
            return 1
        else:
            if (x - a) % d == 0:
                return 0
            else:
                return 1
    if d < 0:
        if a < x:
            return 1
        else:
            if (x - a) % d == 0:
                return 0
            else:
                return 1

=======
Suggestion 7

def problem():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if a == x:
            return 0
        else:
            return 1
    if (x - a) % d == 0:
        if 1 <= (x - a) // d <= n:
            return 0
        else:
            return 1
    else:
        if 1 <= (x - a) // d + 1 <= n:
            return 1
        else:
            if 1 <= (x - a) // d - 1 <= n:
                return 1
            else:
                return 2

print(problem())

=======
Suggestion 8

def main():
    X,A,D,N = map(int, input().split())
    if N == 1:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if X == A:
            print(0)
        else:
            print(1)

=======
Suggestion 9

def solve(x, a, d, n):
    # print(x, a, d, n)
    if d == 0:
        if x != a:
            return -1
        else:
            return 0
    else:
        if n % 2 == 0:
            if x < a:
                return -1
            else:
                if (x - a) % 2 == 0:
                    return 0
                else:
                    return 1
        else:
            if x < a:
                if (a - x) % 2 == 0:
                    return 1
                else:
                    return 2
            else:
                if (x - a) % 2 == 0:
                    return 1
                else:
                    return 2

=======
Suggestion 10

def solve(X, A, D, N):
    return 0
