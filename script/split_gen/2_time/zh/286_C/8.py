def main():
    n, a, b = map(int, input().split())
    s = input()
    if n % 2 == 0:
        if a <= b:
            print(a * n // 2)
        else:
            print(b * n // 2)
    else:
        if a <= b:
            print(a * (n - 1) // 2 + b)
        else:
            print(b * (n - 1) // 2 + b)
