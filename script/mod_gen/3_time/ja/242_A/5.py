def main():
    A, B, C, X = map(int, input().split())
    print(1 - (B - X) / (B - A) * (C - 1) / C)

if __name__ == '__main__':
    main()