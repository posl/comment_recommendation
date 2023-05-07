def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    gcd()