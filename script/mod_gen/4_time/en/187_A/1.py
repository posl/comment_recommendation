def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

if __name__ == '__main__':
    sum_of_digits()