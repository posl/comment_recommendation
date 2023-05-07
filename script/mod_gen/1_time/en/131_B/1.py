def main():
    N, L = map(int, input().split())
    if L <= 0 <= L + N - 1:
        print(sum(range(L, L + N)))
    elif L < L + N - 1:
        print(sum(range(L, L + N - 1)))
    else:
        print(sum(range(L + 1, L + N)))

if __name__ == '__main__':
    main()