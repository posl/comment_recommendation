def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))
ans = 0
for i in range(1, m+1):
    flag = True
    for j in range(len(a)):
        if gcd(a[j], i) != 1:
            flag = False
            break
    if flag:
        ans += 1
        print(i)
print(ans)
