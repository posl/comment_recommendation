def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

if __name__ == '__main__':
    count_digits()