def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)
N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    gcd()