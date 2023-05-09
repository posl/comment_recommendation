def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 2**30
    for i in range(2**(n-1)):
        or_ = 0
        xor_ = 0
        for j in range(n):
            or_ |= a[j]
            if (i >> j) & 1:
                xor_ ^= or_
                or_ = 0
        xor_ ^= or_
        ans = min(ans, xor_)
    print(ans)
