def f(n, m, a, i):
    if i == n:
        print(' '.join(map(str, a)))
        return
    for j in range(1, m+1):
        a[i] = j
        f(n, m, a, i+1)
n, m = map(int, input().split())
a = [0] * n
f(n, m, a, 0)

if __name__ == '__main__':
    f()