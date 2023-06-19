def get_val(a, b):
    c = 0
    for i in range(len(a)):
        c += int(a[i]) * pow(b, len(a) - i - 1)
    return c
x = input()
m = int(input())
d = 0
for i in range(len(x)):
    d = max(d, int(x[i]))
ans = 0
left = d + 1
right = m + 1
while (right - left > 1):
    mid = (left + right) // 2
    if (get_val(x, mid) <= m):
        left = mid
    else:
        right = mid
print(left - d)
