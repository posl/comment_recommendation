def main():
    N, L = map(int, input().split())
    if L > 0:
        print(sum(range(L, L+N)))
    elif L+N-1 < 0:
        print(sum(range(L, L+N)))
    else:
        print(sum(range(L, L+N)) - L)

if __name__ == '__main__':
    main()