def main():
    a, b = map(int, input().split())
    print(b - a - 1 - sum(range(a + 1)))

if __name__ == '__main__':
    main()