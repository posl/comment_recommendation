def is_triangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False
n = int(input())
l = list(map(int, input().split()))
l.sort()
count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if is_triangle(l[i], l[j], l[k]):
                count += 1
print(count)
