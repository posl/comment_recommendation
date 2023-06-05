def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
print(g)

if __name__ == '__main__':
    gcd()