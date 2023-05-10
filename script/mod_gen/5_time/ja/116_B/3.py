def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1]) == 2:
        break
print(len(a))

if __name__ == '__main__':
    f()