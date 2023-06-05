def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    sum_A = sum(A)
    ans = 0
    for a in A:
        sum_A -= a
        ans += a * sum_A
        ans %= MOD
    print(ans)
main()
