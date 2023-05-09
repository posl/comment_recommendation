def solve(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j <= n and i*j == int(i**0.5)**2 * int(j**0.5)**2:
                count += 1
    return count
