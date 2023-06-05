def f(m, a):
    sum = 0
    for i in range(len(a)):
        sum += m % a[i]
    return sum
n = int(input())
a = list(map(int, input().split()))
max = 0
max_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
a.pop(max_index)
m = max
while True:
    if f(m, a) < f(m - 1, a):
        m -= 1
    else:
        break
print(f(m, a))
