def main():
    n, x = map(int, input().split())
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(s[(x-1)%n])

if __name__ == '__main__':
    main()