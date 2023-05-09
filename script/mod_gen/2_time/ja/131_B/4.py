def main():
    N, L = map(int, input().split())
    ans = 0
    if L >= 0:
        ans = sum(i for i in range(L, L+N))
    elif L+N-1 <= 0:
        ans = sum(i for i in range(L, L+N))
    else:
        ans = sum(i for i in range(L, L+N)) - min(i for i in range(L, L+N))
    print(ans)

if __name__ == '__main__':
    main()