def comb(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if r == 1:
        return n
    if r == 0:
        return 1
    return comb(n - 1, r) + comb(n - 1, r - 1)
s = int(input())
ans = 0
for i in range(1,s//3+1):
    ans += comb(s-3*i+i-1,i-1)
    ans %= 10**9+7
print(ans)

if __name__ == '__main__':
    comb()