def sum_digits(num):
    return sum([int(x) for x in str(num)])
A, B = [int(x) for x in input().split()]
print(max(sum_digits(A), sum_digits(B)))

if __name__ == '__main__':
    sum_digits()