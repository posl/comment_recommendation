def main():
    A, B = map(int, input().split())
    num = 1
    while A * num <= B:
        num += 1
    print(num - 1)

if __name__ == '__main__':
    main()