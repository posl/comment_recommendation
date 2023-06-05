def triangle(n):
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]
n = int(input())
for i in triangle(n):
    print(*i)
    if len(i) == n:
        break
