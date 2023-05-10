def expected_value(a, b, c):
    return a / (a + b + c) + b / (a + b + c) * (1 + expected_value(a + 1, b - 1, c)) + c / (a + b + c) * (1 + expected_value(a, b + 1, c - 1))
a, b, c = map(int, input().split())
print(expected_value(a, b, c))

if __name__ == '__main__':
    expected_value()