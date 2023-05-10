def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if ans < cnt:
        ans = cnt
        ans_i = i
print(ans_i)

if __name__ == '__main__':
    gcd()