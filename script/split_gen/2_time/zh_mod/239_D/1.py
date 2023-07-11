def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1): #int(n**0.5)+1 为了提高效率
        if n % i == 0:
            return False
