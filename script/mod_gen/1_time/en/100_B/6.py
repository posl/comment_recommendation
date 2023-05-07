def main():
    D, N = map(int, input().split())
    print(100**D * (N + (N == 100)))

if __name__ == '__main__':
    main()