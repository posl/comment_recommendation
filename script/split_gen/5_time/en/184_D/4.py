def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print(1)
    else:
        print((a / (a + b + c)) * (100 / (a + b + c - 99)) + (b / (a + b + c)) * (100 / (a + b + c - 99)) + (c / (a + b + c)) * (100 / (a + b + c - 99)))
