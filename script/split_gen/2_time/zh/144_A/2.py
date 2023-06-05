def is_triangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    return False
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_triangle(l[i], l[j], l[k]):
                ans += 1
print(ans)
