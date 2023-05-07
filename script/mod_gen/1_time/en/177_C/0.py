def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for a in A:
        S -= a
        ans += a * S
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()