def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if __name__ == '__main__':
    gcd()