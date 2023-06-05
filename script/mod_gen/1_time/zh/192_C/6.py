def f(x):
    g1 = int("".join(sorted(str(x), reverse=True)))
    g2 = int("".join(sorted(str(x))))
    return g1 - g2
n, k = map(int, input().split())
a = n
for _ in range(k):
    a = f(a)
print(a)

if __name__ == '__main__':
    f()