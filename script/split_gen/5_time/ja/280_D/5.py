def f(n):
    if n == 1:
        return 1
    return n * f(n-1)
k = int(input())
n = 1
while True:
    if k <= f(n):
        break
    n += 1
print(n)
