def binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * binary(int(n / 2)))

if __name__ == '__main__':
    binary()