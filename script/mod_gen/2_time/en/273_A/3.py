def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)
N = int(input())
print(f(N))

if __name__ == '__main__':
    f()