def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
N = int(input())
A = list(map(int, input().split()))
max_gcd = 0
max_num = 0
for i in range(2, 1001):
    gcdness = 0
    for a in A:
        if a%i == 0:
            gcdness += 1
    if gcdness > max_gcd:
        max_gcd = gcdness
        max_num = i
print(max_num)
