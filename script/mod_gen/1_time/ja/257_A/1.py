def main():
    n, x = map(int, input().split())
    print(chr((x - 1) // n + ord('A')))

if __name__ == '__main__':
    main()