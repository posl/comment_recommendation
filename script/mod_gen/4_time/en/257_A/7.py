def main():
    n, x = map(int, input().split())
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alpha[x % 26 - 1])

if __name__ == '__main__':
    main()