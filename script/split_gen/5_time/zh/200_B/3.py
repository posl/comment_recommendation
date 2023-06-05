def f(n):
    if n % 200 == 0:
        return n // 200
    else:
        return int(str(n) + '200')
n, k = map(int, input().split())
for i in range(k):
    n = f(n)
print(n)
