def main():
    a, b = map(int, input().split())
    s = (a ** 2 + b ** 2) ** 0.5
    print(a / s, b / s)
