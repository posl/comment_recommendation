def f(n, k, a):
    a = sorted([a[i][j] for i in range(n) for j in range(n)])
    return a[k*k//2]
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(f(n, k, a))

if __name__ == '__main__':
    f()