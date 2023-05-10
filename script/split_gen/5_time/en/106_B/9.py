def divisors(n):
    divisors = [1]
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors
