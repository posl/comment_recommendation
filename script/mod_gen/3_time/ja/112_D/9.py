def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = A[::-1]

if __name__ == '__main__':
    gcd()