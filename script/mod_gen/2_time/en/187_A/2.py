def sum_digits(n):
    return sum([int(i) for i in str(n)])
A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))
A, B = map(int, input().split())

if __name__ == '__main__':
    sum_digits()