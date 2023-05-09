def sum_of_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum
a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

if __name__ == '__main__':
    sum_of_digits()