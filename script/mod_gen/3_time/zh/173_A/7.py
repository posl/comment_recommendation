def get_change(n):
    if n < 1000:
        return 1000 - n
    else:
        return n % 1000

if __name__ == '__main__':
    get_change()