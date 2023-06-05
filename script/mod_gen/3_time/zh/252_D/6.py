def f(n, a):
    c = [0] * (10**5+1)
    for i in a:
        c[i] += 1
    s = sum([i*(i-1)//2*(i-2)//3 for i in c])
    return s
n = int(input())
a = list(map(int, input().split()))
print(f(n, a))
