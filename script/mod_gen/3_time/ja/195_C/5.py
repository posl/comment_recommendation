def main():
    N = int(input())
    ans = 0
    for i in range(1, 17):
        ans += (N // (10 ** (3 * i))) * (i - 1) * (10 ** (3 * (i - 1)))
        ans += max(0, N - (10 ** (3 * i) - 1)) // (10 ** (3 * (i - 1)))
    print(ans)

if __name__ == '__main__':
    main()