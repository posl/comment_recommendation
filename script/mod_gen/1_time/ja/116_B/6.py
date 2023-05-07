def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
m = 0
while True:
    n = f(a[-1])
    if n in a:
        m = a.index(n)
        break
    a.append(n)
print(m + 1)

if __name__ == '__main__':
    f()