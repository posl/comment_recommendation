def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
N, M = map(int, input().split())
A = list(map(int, input().split()))

if __name__ == '__main__':
    gcd()