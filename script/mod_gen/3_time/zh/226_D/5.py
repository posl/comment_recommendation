def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

if __name__ == '__main__':
    gcd()