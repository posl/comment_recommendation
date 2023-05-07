def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
gcd_list = [0]*1001
for i in range(2, 1001):
    for j in range(n):
        if a[j] % i == 0:
            gcd_list[i] += 1
print(gcd_list.index(max(gcd_list)))

if __name__ == '__main__':
    gcd()