def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))

if __name__ == '__main__':
    gcd()