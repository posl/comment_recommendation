def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
A, B = map(int, input().split())

if __name__ == '__main__':
    sum_digits()