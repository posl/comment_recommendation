def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(10 * 9 ** (n - 1) - 9 ** n + 10 ** n - 10 ** (n - 1))
