def S(n):
    sum = 0
    while n:
        sum += n%10
        n = n/10
    return sum
