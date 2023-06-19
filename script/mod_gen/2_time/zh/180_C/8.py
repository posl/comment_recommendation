def get_divisor(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n // i)
    return sorted(divisor)

if __name__ == '__main__':
    get_divisor()