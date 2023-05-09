def main():
    N, L = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        ans += L + i - 1
    if L <= 0 and 0 <= L + N - 1:
        print(ans)
    elif L > 0:
        print(ans - L)
    else:
        print(ans - (L + N - 1))

if __name__ == '__main__':
    main()