def main():
    N, L = map(int, input().split())
    if L > 0:
        ans = sum([L + i - 1 for i in range(1, N)])
    elif L + N - 1 < 0:
        ans = sum([L + i - 1 for i in range(1, N)])
    else:
        ans = sum([L + i - 1 for i in range(2, N + 1)])
    print(ans)

if __name__ == '__main__':
    main()