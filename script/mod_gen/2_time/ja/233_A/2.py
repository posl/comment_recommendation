def main():
    X, Y = map(int, input().split())
    print((Y + 9) // 10 - X // 10)

if __name__ == '__main__':
    main()