def main():
    a, b, c = map(int, input().split())
    print(100.0 * (a * b + b * c + c * a) / (a + b + c) / (a + b + c))
