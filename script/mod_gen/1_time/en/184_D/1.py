def main():
    A, B, C = map(int, input().split())
    print((A * (A + 1) / (2 * A + B + C)) + (B * (B + 1) / (2 * B + C)) + (C * (C + 1) / (2 * C)))

if __name__ == '__main__':
    main()