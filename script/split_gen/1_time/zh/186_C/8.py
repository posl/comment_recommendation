def f(n):
    s = 0
    for i in range(1,n+1):
        if '7' in str(i) or '7' in oct(i):
            s += 1
    return n-s
N = int(input())
print(f(N))
