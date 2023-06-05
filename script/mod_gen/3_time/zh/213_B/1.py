def main():
    n = int(input())
    a = list(map(int, input().split()))
    # a = [1, 123, 12345, 12, 1234, 123456]
    # a = [3, 1, 4, 15, 9]
    b = sorted(a)
    print(a.index(b[1]) + 1)

if __name__ == '__main__':
    main()