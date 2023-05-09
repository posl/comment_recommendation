def sum_digits(n):
    return sum(int(i) for i in str(n))
n = int(input())

if __name__ == '__main__':
    sum_digits()