def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

if __name__ == '__main__':
    permutations_count()