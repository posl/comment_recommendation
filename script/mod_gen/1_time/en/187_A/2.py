def sum_digits(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s
a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

if __name__ == '__main__':
    sum_digits()