def main():
    a, b = map(int, input().split())
    if a < b:
        print(a * 10 ** b)
    else:
        print(b * 10 ** a)

if __name__ == '__main__':
    main()