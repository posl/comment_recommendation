def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
N,M = map(int, input().split())
for i in range(1, int(M**0.5)+1):
    if M%i == 0:
        if M//i >= N:
            ans = i
        if i >= N:
            ans = M//i
print(ans)

if __name__ == '__main__':
    gcd()