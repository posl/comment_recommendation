def comb(n, r):
    if n < r: return 0
    r = min(r, n-r)
    if r == 0: return 1
    if r == 1: return n
    numerator = [n-r+1-i for i in range(r)]
    denominator = [i+1 for i in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p-1]
        if pivot > 1:
            offset = (n-r)%p
            for k in range(p-1,r,p):
                numerator[k-offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for i in range(r):
        if numerator[i] > 1:
            result *= numerator[i]
    return result
n, k = map(int, input().split())
mod = 10**9+7
for i in range(1, k+1):
    if n-k+1 < i:
        print(0)
    else:
        print(comb(n-k+1, i)*comb(k-1, i-1)%mod)

if __name__ == '__main__':
    comb()