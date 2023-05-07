def main():
    n = int(input())
    print(n // 100)
    print(n % 100 // 10)
    print(n % 10)
    print(n % 100 % 10)
    print(n % 10 * 100 + n % 100 // 10 * 10 + n // 100)
