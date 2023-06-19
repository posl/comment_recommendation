def main():
    a, b = map(int, input().split())
    if b <= 2*a + 100:
        print(2*a + 100 - b)
    else:
        print(0)

if __name__ == '__main__':
    main()