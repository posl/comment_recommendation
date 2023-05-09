def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    ans = 0
    for a in range(2, int(N ** 0.5) + 1):
        b = 2
        while a ** b <= N:
            ans += 1
            b += 1
    print(N - ans)

if __name__ == '__main__':
    main()