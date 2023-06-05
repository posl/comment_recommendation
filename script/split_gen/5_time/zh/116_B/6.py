def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(f(a[i - 2]))
    if a.count(a[i - 1]) == 2:
        break
print(i)
