def sum_digits(num):
    return sum(int(x) for x in str(num))

if __name__ == '__main__':
    sum_digits()