def main():
    n = int(input())
    print((9 ** n + 9 ** n - 8 ** n) % (10 ** 9 + 7))
