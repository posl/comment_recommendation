def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
i = 1
while a[i-1] not in a[0:i-1]:
    a.append(f(a[i-1]))
    i += 1
print(i)
