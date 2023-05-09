def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
k = int(input())
n = 1
while True:
    if f(n) % k == 0:
        print(n)
        break
    else:
        n += 1
