def main():
    n, x = map(int, input().split())
    n = n - 1
    x = x - 1
    print(chr(65 + x % 26))
