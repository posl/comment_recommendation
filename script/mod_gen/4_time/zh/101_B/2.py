def s(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == '__main__':
    s()