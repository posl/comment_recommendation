def main():
    N, M = map(int, input().split())
    MOD = 10**9+7
    ans = 1
    for i in range(2, M+1):
        cnt = 0
        while M%i == 0:
            cnt += 1
            M //= i
        ans *= cnt+N-1
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()