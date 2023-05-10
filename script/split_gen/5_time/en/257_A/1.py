def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + x // n - 1))
