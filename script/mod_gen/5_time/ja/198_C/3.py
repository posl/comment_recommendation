def main():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) < R**2:
        print(2)
    else:
        print(int(((X**2 + Y**2)**0.5 + R - 1)//R))

if __name__ == '__main__':
    main()