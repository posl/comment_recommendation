def getDivisors(n):
    divisors = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors += 2
    if n**0.5 == int(n**0.5):
        divisors -= 1
    return divisors
