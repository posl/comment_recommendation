def main():
    X, Y = map(int, input().split())
    print((Y-X%Y)%Y)

if __name__ == '__main__':
    main()