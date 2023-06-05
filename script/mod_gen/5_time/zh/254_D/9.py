def problem254_d(N):
    from math import sqrt
    from collections import Counter
    from functools import reduce
    from operator import mul
    from itertools import combinations
    def prime_factorization(n):
        i = 2
        table = []
        while i * i <= n:
            while n % i == 0:
                n //= i
                table.append(i)
            i += 1
        if n > 1:
            table.append(n)
        return table
    def divisors(n):
        i = 1
        table = []
        while i * i <= n:
            if n % i == 0:
                table.append(i)
                if i * i != n:
                    table.append(n // i)
            i += 1
        table.sort()
        return table
    def prime_factorization_exponent(n):
        i = 2
        table = []
        while i * i <= n:
            while n % i == 0:
                n //= i
                table.append(i)
            i += 1
        if n > 1:
            table.append(n)
        return Counter(table)
    def combination_with_repetition(n, r):
        from math import factorial
        return factorial(n + r - 1) // factorial(r) // factorial(n - 1)
    def combination(n, r):
        from math import factorial
        return factorial(n) // factorial(r) // factorial(n - r)
    def combination_with_repetition_exponent(n, r):
        return Counter(prime_factorization_exponent(n + r - 1)) - Counter(prime_factorization_exponent(r)) - Counter(prime_factorization_exponent(n - 1))
    def combination_exponent(n, r):
        return Counter(prime_factorization_exponent(n)) - Counter(prime_factorization_exponent(r)) - Counter(prime_factorization_exponent(n - r))
    def product(numbers):
        return reduce(mul, numbers, 1)
    def square_free_number(n):
        return all(v == 1 for v in prime_factorization_exponent(n).values())
    def square_free_number_exponent(n):
        return Counter({k: 1 for k in prime_factorization_exponent(n)})
    def square_number(n):
        return all(v % 2 == 0 for v in prime_factorization_exponent(n).values())
    def square_number_exponent(n

if __name__ == '__main__':
    problem254_d()