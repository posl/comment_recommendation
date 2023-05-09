def main():
    X, Y = map(int, input().split())
    print((Y - 1) // 10 - X // 10)

if __name__ == '__main__':
    main()