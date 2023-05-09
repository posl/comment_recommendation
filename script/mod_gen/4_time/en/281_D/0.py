def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, K, D = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(N, K, D)
# print(A)
g = gcd(K, D)
# print(g)

if __name__ == '__main__':
    gcd()