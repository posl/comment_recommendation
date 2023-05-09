def main():
    X, Y, R = map(float, input().split())
    print(int(R**2 - X**2 - Y**2 + 1))

if __name__ == '__main__':
    main()