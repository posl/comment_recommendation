def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, A, B = map(int, input().split())
g = gcd(A, B)
print(N - N // A - N // B + N // (A * B // g))

if __name__ == '__main__':
    gcd()