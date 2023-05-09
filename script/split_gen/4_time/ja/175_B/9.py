def checkTriangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if checkTriangle(a[i], a[j], a[k]) and a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                ans += 1
print(ans)
