def sumDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumDigits(n // 10)

if __name__ == '__main__':
    sumDigits()