def f(n):
    if n == 0:
        return 1
    return n * f(n-1)
n = int(input())
print(f(n))

if __name__ == '__main__':
    f()