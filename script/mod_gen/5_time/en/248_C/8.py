def find_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

if __name__ == '__main__':
    find_factorial()