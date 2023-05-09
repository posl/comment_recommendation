def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
while True:
    if f(a[-1]) in a:
        print(len(a) + 1)
        exit()
    else:
        a.append(f(a[-1]))
