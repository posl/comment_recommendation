def divisor(n):
    if n == 1:
        return [1]
    divisors = [1, n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

if __name__ == '__main__':
    divisor()