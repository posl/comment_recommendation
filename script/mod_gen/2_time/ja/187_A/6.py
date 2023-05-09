def sum_digit(num):
    return sum(map(int, str(num)))
A, B = map(int, input().split())
print(max(sum_digit(A), sum_digit(B)))

if __name__ == '__main__':
    sum_digit()