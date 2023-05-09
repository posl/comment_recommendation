def main():
    a, b, c = map(int, input().split())
    print(100 * a / (a+b+c) + 100 * b / (a+b+c) + 100 * c / (a+b+c) - 3)
