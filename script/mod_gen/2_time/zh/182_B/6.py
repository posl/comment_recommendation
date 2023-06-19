def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(2, 1001):
    temp = 0
    for j in range(n):
        if a[j] % i == 0:
            temp += 1
    if cnt < temp:
        ans = i
        cnt = temp
print(ans)

if __name__ == '__main__':
    gcd()