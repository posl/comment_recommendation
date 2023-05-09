def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [a//2 for a in A]
lcm = 1
for a in A:
    lcm = lcm * a // gcd(lcm,a)
for a in A:
    if (lcm//a)%2==0:
        print(0)
        exit()
print((M//lcm+1)//2)

if __name__ == '__main__':
    gcd()