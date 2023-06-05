def main():
    N, L = map(int, input().split())
    print(sum(range(L + 1, L + N)) - min(range(L + 1, L + N), key=abs))

if __name__ == '__main__':
    main()