def get_factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * get_factorial(n-1)

if __name__ == '__main__':
    get_factorial()