def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N=int(input())
print(2*N//gcd(2,N))

if __name__ == '__main__':
    gcd()