def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for a in A:
            if a & (1 << i):
                c += 1
        ans += c * (N - c) * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)
main()

if __name__ == '__main__':
    main()