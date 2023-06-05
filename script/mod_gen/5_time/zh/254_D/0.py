def f(n):
    n = int(n)
    l = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j == n:
                l.append((i,j))
    return len(l)

if __name__ == '__main__':
    f()