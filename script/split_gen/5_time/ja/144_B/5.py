def check(n):
    for i in range(1, 10):
        if n % i == 0 and n / i in range(1, 10):
            return True
    return False
n = int(input())
print('Yes' if check(n) else 'No')
