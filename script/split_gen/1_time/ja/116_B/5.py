def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
n = 1
while True:
    a.append(f(a[n-1]))
    if a[n-1] in a[:n-1]:
        print(n)
        break
    n += 1
