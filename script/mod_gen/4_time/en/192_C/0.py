def f(x):
    g1 = int(''.join(sorted(str(x), reverse=True)))
    g2 = int(''.join(sorted(str(x))))
    return g1 - g2
N, K = map(int, input().split())
for i in range(K):
    N = f(N)
print(N)

if __name__ == '__main__':
    f()