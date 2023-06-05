def f(n, a, b):
    lcm = a * b / gcd(a, b)
    return n - n / a - n / b + n / lcm
