def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    z = (x + 1) % 3
    if z == y:
        print(x)
    else:
        print(z)

if __name__ == '__main__':
    main()