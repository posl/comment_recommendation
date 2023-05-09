def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

if __name__ == '__main__':
    sum_digits()