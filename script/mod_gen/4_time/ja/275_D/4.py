def f(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return f(n//2) + f(n//3)
    else:
        return f(n//2)
n = int(input())
print(f(n))

if __name__ == '__main__':
    f()