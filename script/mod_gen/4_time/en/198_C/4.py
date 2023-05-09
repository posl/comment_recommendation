def main():
    R, X, Y = map(int, input().split())
    import math
    if (X**2 + Y**2) % R**2 == 0:
        print(int(math.sqrt(X**2 + Y**2) // R))
    else:
        print(int(math.sqrt(X**2 + Y**2) // R + 1))

if __name__ == '__main__':
    main()