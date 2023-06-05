def main():
    a, b = map(int, input().split())
    x = 1
    y = 1
    if a != 0:
        x = (a**2 / (a**2 + b**2))**0.5
        y = (b**2 / (a**2 + b**2))**0.5
    print("{:.12f} {:.12f}".format(x, y))

if __name__ == '__main__':
    main()