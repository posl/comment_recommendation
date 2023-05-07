def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x
    
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
max_gcd = 0
for i in range(2, a[0]+1):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if count > max_gcd:
        max_gcd = count
        ans = i
        
print(ans)
