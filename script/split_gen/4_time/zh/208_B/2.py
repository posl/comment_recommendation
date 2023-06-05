def main():
    p = int(input())
    n = 0
    for i in range(10, 0, -1):
        n += p // factorial(i)
        p %= factorial(i)
    print(n)
