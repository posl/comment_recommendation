def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 1
    for i in range(N):
        ans *= C[i]-i
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()