def is_in_range(n):
    if -2**31 <= n and n <= 2**31 - 1:
        return True
    else:
        return False

if __name__ == '__main__':
    is_in_range()