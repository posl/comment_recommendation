def print_last_two_digits(n):
    if n < 100 or n > 999:
        return
    print(n % 100)

if __name__ == '__main__':
    print_last_two_digits()