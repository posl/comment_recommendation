def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

if __name__ == '__main__':
    count_digits()