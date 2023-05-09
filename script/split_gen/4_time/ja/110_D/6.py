def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            cnt = 0
            while m % i == 0:
                cnt += 1
                m //= i
            ans *= cmb(n+cnt-1, cnt)
            ans %= mod
    if m != 1:
        ans *= cmb(n, 1)
        ans %= mod
    print(ans)
mod = 10**9 + 7
n_max = 10**5 + 100
fac = [0] * n_max
finv = [0] * n_max
inv = [0] * n_max
