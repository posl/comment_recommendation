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
    if a[i] in a[:i]:
        print(a.index(a[i]) + 1)
        break
    i += 1
