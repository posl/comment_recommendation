def main():
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    if x > y and x > z:
        if y < z:
            print(x - y)
        else:
            print(x - z)
    elif y > x and y > z:
        if x < z:
            print(y - x)
        else:
            print(y - z)
    elif z > x and z > y:
        if x < y:
            print(z - x)
        else:
            print(z - y)
    else:
        print(-1)

if __name__ == '__main__':
    main()