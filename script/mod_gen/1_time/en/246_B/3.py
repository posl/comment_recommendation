def main():
    A, B = map(int, input().split())
    d = (A**2 + B**2)**(0.5)
    x = A / d
    y = B / d
    print(x, y)

if __name__ == '__main__':
    main()