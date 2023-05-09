def is_square(n):
    return n**.5 == int(n**.5)
n = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        if is_square(i*j):
            if i == j:
                ans += 1
            else:
                ans += 2
print(ans)
