def is753(n):
    if n < 10:
        return (n == 3) or (n == 5) or (n == 7)
    else:
        return is753(n % 10) and is753(n // 10)

if __name__ == '__main__':
    is753()