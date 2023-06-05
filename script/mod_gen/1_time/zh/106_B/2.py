def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if num/i != i:
                divisors.append(num/i)
    return divisors

if __name__ == '__main__':
    get_divisors()