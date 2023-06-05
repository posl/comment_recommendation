def f(n):
    if n == 1:
        return [1]
    else:
        tmp = f(n-1)
        return tmp + [n] + tmp
n = int(input())
print(' '.join(map(str, f(n))))
