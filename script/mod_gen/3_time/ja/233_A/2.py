def main():
    X, Y = map(int, input().split())
    if X % 10 == 0:
        print(0)
    else:
        print(10 - X % 10)

if __name__ == '__main__':
    main()