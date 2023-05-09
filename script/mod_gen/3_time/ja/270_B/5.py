def main():
    x, y, z = map(int, input().split())
    if abs(x) < abs(y):
        if abs(x) < abs(z):
            print(abs(z - x))
        else:
            print(abs(x - z))
    else:
        if abs(y) < abs(z):
            print(abs(z - y))
        else:
            print(abs(y - z))

if __name__ == '__main__':
    main()