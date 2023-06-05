def max_sum():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))
    return

if __name__ == '__main__':
    max_sum()