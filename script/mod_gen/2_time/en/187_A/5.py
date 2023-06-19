def sum_of_digits(x):
    return sum(int(d) for d in str(x))
a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))
