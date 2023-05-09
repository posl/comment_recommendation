def main():
    a, b, c = map(int, input().split())
    print(max(a + b * 10 + c, a * 10 + b + c, a + b + c * 10))
