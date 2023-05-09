def main():
    N, M = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(2, M + 1):
        cnt = 0
        while M % i == 0:
            M //= i
            cnt += 1
        ans = ans * (cnt + 1) % mod
    print(ans)

if __name__ == '__main__':
    main()