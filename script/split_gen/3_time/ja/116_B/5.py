def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
i = 1
while True:
    a.append(f(a[i - 1]))
    if len(a) != len(set(a)):
        break
    i += 1
print(len(a))
