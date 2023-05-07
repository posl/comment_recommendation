def main():
    N, K = map(int, input().split())
    print(len(str(N)))
    print(len(str(N)) if N == 0 else len(str(N)) - 1)

if __name__ == '__main__':
    main()