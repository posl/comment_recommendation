def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
A, B = map(int, input().split())
print(A * B // gcd(A, B))
I have a problem with this code. I have a problem with this code.

if __name__ == '__main__':
    gcd()