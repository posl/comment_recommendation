def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
N = int(input())
ans = 2*N//gcd(2,N)
print(ans)

if __name__ == '__main__':
    gcd()