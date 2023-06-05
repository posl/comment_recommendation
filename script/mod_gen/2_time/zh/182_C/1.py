def gcd(a, b):
    if a<b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in a:
        if j%i==0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        res = i
print(res)

if __name__ == '__main__':
    gcd()