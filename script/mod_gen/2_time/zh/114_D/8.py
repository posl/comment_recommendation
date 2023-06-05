def is753(n):
    if n % 10 == 3 or n % 10 == 5 or n % 10 == 7:
        return True
    elif n >= 10:
        return is753(n // 10)
    else:
        return False

if __name__ == '__main__':
    is753()