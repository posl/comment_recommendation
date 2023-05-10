def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
n, m = map(int, input().split())
a = m//n
while True:
    if m%a == 0:
        print(a)
        break
    else:
        a -= 1

if __name__ == '__main__':
    gcd()