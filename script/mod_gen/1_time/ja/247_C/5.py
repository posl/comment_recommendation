def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)
N = int(input())
print(*f(N))

if __name__ == '__main__':
    f()