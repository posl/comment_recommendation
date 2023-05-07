def main():
    # data load
    a, b, c = map(int, input().split())
    print(10 * max(a, b, c) + a + b + c)

if __name__ == '__main__':
    main()