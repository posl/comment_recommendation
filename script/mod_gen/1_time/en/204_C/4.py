def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = N * (N - 1)
    for a, b in AB:
        if a > b:
            a, b = b, a
        ans -= (N - a) * (N - b)
    print(ans)

if __name__ == '__main__':
    main()