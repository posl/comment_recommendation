def main():
    A, B = map(int, input().split())
    x = (A**2 - B**2)/(2*A)
    y = (A**2 - x**2)**0.5
    print(x, y)

if __name__ == '__main__':
    main()