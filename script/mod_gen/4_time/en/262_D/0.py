def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
M = 998244353

if __name__ == '__main__':
    gcd()