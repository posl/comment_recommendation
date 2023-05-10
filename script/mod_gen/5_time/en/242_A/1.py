def problems242_a():
    a, b, c, x = map(int, input().split())
    if a > x:
        print(0)
    elif a <= x <= b:
        print(c / (b - a + 1))
    else:
        print(1)

if __name__ == '__main__':
    problems242_a()