def combination_mod(n, r, mod):
    if n < r:
        return 0
    elif n < 0 or r < 0:
        return 0
    elif n == 0 or r == 0:
        return 1
    else:
        return (fact[n] * factinv[r] * factinv[n-r]) % mod
n,k = map(int,input().split())
mod = 10**9+7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, n+k+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[i]) % mod)
ans = 0
for i in range(k,n+2):
    ans += combination_mod(n+1,i,mod)*combination_mod(n,i-1,mod)
    ans %= mod
print(ans)

if __name__ == '__main__':
    combination_mod()