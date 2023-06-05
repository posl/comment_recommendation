def solve(n):
    count = 0
    for c in range(1, n):
        if n % c == 0:
            count += n // c - 1
        else:
            count += n // c
    return count
