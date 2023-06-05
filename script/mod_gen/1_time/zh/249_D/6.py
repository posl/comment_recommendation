def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    gcd()