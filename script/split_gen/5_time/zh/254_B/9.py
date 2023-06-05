def f(n):
    if n == 1:
        return [[1]]
    else:
        L = f(n-1)
        L.append([1] + [L[-1][i-1] + L[-1][i] for i in range(1, n-1)] + [1])
        return L
n = int(input())
for i in f(n):
    print(' '.join(map(str, i)))
