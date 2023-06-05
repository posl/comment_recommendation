def f(x):
    g1 = int(''.join(sorted(str(x), reverse=True)))
    g2 = int(''.join(sorted(str(x))))
    return g1 - g2
N, K = map(int, input().split())
a = [N]
for i in range(1, K + 1):
    a.append(f(a[i - 1]))
print(a[K])
