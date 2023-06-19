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
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        break
print(i)

if __name__ == '__main__':
    f()