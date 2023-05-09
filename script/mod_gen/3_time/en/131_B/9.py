def main():
    N, L = map(int, input().split())
    print(sum(range(L, L+N)) - (L-1 if L <= 0 <= L+N-1 else (L+N-1 if 0 <= L+N-1 else 0)))

if __name__ == '__main__':
    main()