def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
A,B = map(int,input().split())
print(A*B//gcd(A,B))

if __name__ == '__main__':
    gcd()