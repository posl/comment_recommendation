def main():
    a, b = map(int, input().split())
    total = b * (b + 1) // 2 - a * (a - 1) // 2
    print(total - b + a - 1)
main()

if __name__ == '__main__':
    main()