def main():
    import sys
    import math
    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1: a.append(n)
        return a
    def solve(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve(n - 2)
    def solve2(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve2(n - 2)
    def solve3(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve3(n - 2)
    def solve4(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve4(n - 2)
    def solve5(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve5(n - 2)
    def solve6(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve6(n - 2)
    def solve7(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve7(n - 2)
    def solve8(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve8(n - 2)
    def solve9(n):
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            return n * solve9(n - 2)
    def solve10(n):
