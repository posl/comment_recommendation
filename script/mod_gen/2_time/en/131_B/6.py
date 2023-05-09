def main():
    N, L = map(int, input().split())
    ans = 0
    if L <= 0 <= L + N - 1:
        ans = sum(range(L, L + N))
    elif L > 0:
        ans = sum(range(L, L + N - 1))
    else:
        ans = sum(range(L + 1, L + N))
    print(ans)

if __name__ == '__main__':
    main()