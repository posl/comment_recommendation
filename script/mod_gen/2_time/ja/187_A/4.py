def sum_digits(n):
    return sum([int(d) for d in str(n)])
A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

if __name__ == '__main__':
    sum_digits()