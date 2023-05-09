def main():
    MOD = 10**9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    ans = 0
    for a in A:
        sumA -= a
        ans += a * sumA
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()