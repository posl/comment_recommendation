def main():
    n, x = map(int, input().split())
    print(chr(65 + x // n - 1))
