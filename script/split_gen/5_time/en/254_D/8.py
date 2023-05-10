def is_square(n):
    return n == int(n**.5)**2
n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if is_square(i*j):
            ans += 1
print(ans)
