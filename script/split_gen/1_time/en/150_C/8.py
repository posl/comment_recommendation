def get_permutation(n, index):
    """Return the index-th permutation of (1,2,...,n)."""
    if n == 1:
        return [1]
    else:
        fact = 1
        for i in range(2, n):
            fact *= i
        remainder = index % fact
        quotient = index // fact
        if remainder == 0:
            quotient -= 1
            remainder = fact
        return [quotient + 1] + get_permutation(n - 1, remainder)
