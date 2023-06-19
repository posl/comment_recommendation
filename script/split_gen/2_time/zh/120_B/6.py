def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a, b, k = map(int, input().split())
gcd = gcd(a, b)
gcd_list = []
for i in range(1, gcd + 1):
    if gcd % i == 0:
        gcd_list.append(i)
print(gcd_list[-k])
