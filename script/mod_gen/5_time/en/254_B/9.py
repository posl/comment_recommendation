def f(n):
    if n == 0:
        return [1]
    else:
        a = f(n-1)
        return [1] + [a[i-1] + a[i] for i in range(1, n)] + [1]
n = int(input())
for i in range(n):
    print(*f(i))

if __name__ == '__main__':
    f()