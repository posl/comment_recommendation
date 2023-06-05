def main():
    n, a, b = map(int, input().split())
    if a > b:
        print(0)
    elif a == b:
        print(1)
    else:
        print(n * a // (a + b))

if __name__ == '__main__':
    main()