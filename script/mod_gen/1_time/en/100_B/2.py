def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(N * 100**D)
main()

if __name__ == '__main__':
    main()