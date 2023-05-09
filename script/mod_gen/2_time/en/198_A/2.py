def divide_sweets(n):
    if n == 1:
        return 0
    elif n%2 == 0:
        return n//2 - 1
    else:
        return n//2

if __name__ == '__main__':
    divide_sweets()