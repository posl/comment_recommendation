def main():
    N, L = map(int, input().split())
    print(sum(range(L + N - 1, L - 1, -1)) - min(range(L + N - 1, L - 1, -1), key=abs))

if __name__ == '__main__':
    main()