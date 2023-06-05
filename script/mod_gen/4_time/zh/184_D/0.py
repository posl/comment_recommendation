def get_expectation(a, b, c):
    if a + b + c == 0:
        return 0
    return (a * get_expectation(a - 1, b, c) + b * get_expectation(a + 1, b - 1, c) + c * get_expectation(a, b + 1, c - 1)) / (a + b + c) + 1

if __name__ == '__main__':
    get_expectation()