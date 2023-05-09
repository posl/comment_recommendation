def main():
    a, b = map(int, input().split())
    print(b - a - int((b - a) * (b - a + 1) / 2))
