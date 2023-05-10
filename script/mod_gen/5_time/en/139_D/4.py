def calc(n):
    a = n // 2
    b = n % 2
    return a * (a + 1) + b
n = int(input())
print(calc(n))

if __name__ == '__main__':
    calc()