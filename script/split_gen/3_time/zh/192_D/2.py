def change_to_num(x, n):
    y = 0
    for i in range(len(x)):
        y = y * n + int(x[i])
    return y
x = input()
m = int(input())
d = 0
for i in range(len(x)):
    d = max(d, int(x[i]))
n = d + 1
while True:
    if change_to_num(x, n) > m:
        break
    n += 1
print(n - d - 1)
