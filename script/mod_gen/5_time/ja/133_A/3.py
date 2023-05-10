def main():
    n, a, b = map(int, input().split())
    if n * a < b:
        print(n * a)
    else:
        print(b)

if __name__ == '__main__':
    main()