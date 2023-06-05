def solve(n):
    if n % 2 == 0:
        if n % 4 == 0:
            return int(n/4), 2
        else:
            return int(n/2), 2
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            if n % (i**2) == 0:
                return int(n/(i**2)), i
            else:
                return n//i, i
    return n, 1
