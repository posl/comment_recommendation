def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += 999 * i * 10 ** (i - 1)
    ans += (N - 10 ** (len(str(N)) - 1) + 1) * len(str(N))
    print(ans)

if __name__ == '__main__':
    main()