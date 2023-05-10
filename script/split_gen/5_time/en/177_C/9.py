def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    sum_a = sum(a)
    sum_a_square = sum([a_i**2 for a_i in a])
    ans = 0
    for a_i in a:
        sum_a -= a_i
        sum_a_square -= a_i**2
        ans += a_i * sum_a
        ans += a_i**2 * (n-1)
        ans -= 2 * a_i * sum_a
        ans %= mod
    print(ans)
