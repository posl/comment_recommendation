def f(n,k,a):
    b = []
    for i in range(n):
        b.append(a[i] ^ k)
    return sum(b)
n,k = map(int,input().split())
a = list(map(int,input().split()))
print(f(n,k,a))
