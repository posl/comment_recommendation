def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1
s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

if __name__ == '__main__':
    f()