def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    gcd()