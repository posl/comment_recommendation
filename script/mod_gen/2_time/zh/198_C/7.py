def main():
    R, X, Y = map(int, input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print((X**2 + Y**2)**(1/2) // R + 1)

if __name__ == '__main__':
    main()