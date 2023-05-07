def calc_combination(n, r):
    return calc_factorial(n) // (calc_factorial(n - r) * calc_factorial(r))
