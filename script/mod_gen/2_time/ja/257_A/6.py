def main():
    N, X = map(int, input().split())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alphabet[(X-1) % 26])

if __name__ == '__main__':
    main()