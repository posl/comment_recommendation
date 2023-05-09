def sum_digits(n):
    return sum(int(d) for d in str(n))
a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

if __name__ == '__main__':
    sum_digits()