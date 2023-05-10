def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
print(N * 2 // gcd(2, N))

if __name__ == '__main__':
    gcd()