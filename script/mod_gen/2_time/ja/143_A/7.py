def main():
    a, b = map(int, input().split())
    print(a - 2 * b if 2 * b <= a else 0)

if __name__ == '__main__':
    main()