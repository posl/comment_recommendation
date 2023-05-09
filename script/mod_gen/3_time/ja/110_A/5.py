def main():
    a, b, c = list(map(int, input().split()))
    print(10 * max(a, b, c) + a + b + c)

if __name__ == '__main__':
    main()