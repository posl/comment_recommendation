def problems242_a():
    a, b, c, x = map(int, input().split())
    if a >= x:
        print(1)
    else:
        print(((b - a) * c) / (b - a) * (b - a + 1) / 2 / (b - a + 1) + (x - b) / (1000 - b))

if __name__ == '__main__':
    problems242_a()