def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input())))

if __name__ == '__main__':
    factorial()