def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum
n = int(input())

if __name__ == '__main__':
    sum_of_digits()