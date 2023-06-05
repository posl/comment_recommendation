def sum(N):
    sum = 0
    for i in range(1, N+1):
        sum += i * f(i)
    return sum
