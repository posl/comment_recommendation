def f(x):
    x = str(x)
    g1 = ''.join(sorted(x, reverse=True))
    g2 = ''.join(sorted(x))
    return int(g1) - int(g2)
N, K = map(int, input().split())
a = N
for i in range(K):
    a = f(a)
print(a)
I think this is the best solution for this problem.
