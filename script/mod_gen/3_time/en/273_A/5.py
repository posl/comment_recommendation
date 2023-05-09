def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
print(f(int(input())))

if __name__ == '__main__':
    f()