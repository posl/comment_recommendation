def main():
    a, b, n = map(int, input().split())
    if n < b:
        print(a * n // b)
    else:
        print(a * (b - 1) // b)
