def main():
    N, L = map(int, input().split())
    ans = 0
    if L <= 0 <= L+N-1:
        ans = 0
    elif L+N-1 < 0:
        ans = sum(range(L, L+N))
    elif 0 < L:
        ans = sum(range(L, L+N-1))
    print(ans)
main()

if __name__ == '__main__':
    main()