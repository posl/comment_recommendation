def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(1, m + 1):
    flag = True
    for j in range(n):
        if gcd(a[j], i) != 1:
            flag = False
            break
    if flag:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)

if __name__ == '__main__':
    gcd()