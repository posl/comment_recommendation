def f(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            s += 1
    return s
N = int(input())
s = 0
for k in range(1, N+1):
    s += k * f(k)
print(s)
