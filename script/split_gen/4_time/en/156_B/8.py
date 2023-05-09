def solve(n,k):
    count = 0
    while n > 0:
        n = n // k
        count += 1
    return count
